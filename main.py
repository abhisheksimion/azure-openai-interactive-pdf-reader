import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import PyPDF2
from tempfile import NamedTemporaryFile
import json

pdf_text = ''

# Import the tool registry
from tool_registry import tool_registry

# Load environment variables from .env file
load_dotenv()

azure_api_key = os.getenv('AZURE_API_KEY')
azure_endpoint = os.getenv('AZURE_ENDPOINT')
azure_api_version = os.getenv('AZURE_API_VERSION')
model_name = os.getenv('MODEL_NAME')

client = AzureOpenAI(
    api_key=azure_api_key,
    api_version=azure_api_version,
    azure_endpoint=azure_endpoint
)

# Define the system prompt
def get_system_prompt():
    return """You are a personal assistant to a developer. Your role is to answer user questions politely and competently.
    You should follow these instructions to solve the case:
    - You are provided with a PDF text to extract information.
    - Understand the ask and get relevant instructions.
    - Follow the instructions to provide solutions to users.
    - Never modify the user query.
    - Never modify the answer generated from the tool. However, make the content more user-friendly by formatting it in markdown, including headers, bullet points, and other markdown elements as appropriate.

    Only call a tool once in a single message.
    If you don't find an answer from the provided PDF document text, give a clear, say 'I cannot answer.' Never provide any dummy values.
    """

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text


# Example usage:
def getPdfContent(pdf_file):
    with NamedTemporaryFile(suffix="pdf", delete=True) as temp:
        temp_name = temp.name
        print(temp_name)

    pdf_file_path = pdf_file
    pdf_text = extract_text_from_pdf(pdf_file_path)
    return pdf_text


# Initialize the messages list with the system prompt and PDF text
messages = [
    {
        "role": "system",
        "content": get_system_prompt()
    },
    {
        "role": "user",
        "content": f'''PDF text: {pdf_text}'''
    }
]


def ask_question(local_messages, user_query):
    # Append the new user query to the messages list
    local_messages.append({
        "role": "user",
        "content": user_query
    })

    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=local_messages,
            temperature=0,
            max_tokens=500,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
        )

        final_result = json.loads(response.model_dump_json(indent=2))
        model_reply = final_result['choices'][0]['message']['content']

        # Check if the model wants to call a function
        if any(tool_name in model_reply for tool_name in tool_registry.tools):
            for tool_name in tool_registry.tools:
                if tool_name in model_reply:
                    # Extract parameters from the reply (this assumes parameters are provided in the model_reply in a JSON-like format)
                    try:
                        parameters_start = model_reply.index('{')
                        parameters_end = model_reply.rindex('}') + 1
                        parameters = json.loads(model_reply[parameters_start:parameters_end])

                        tool_response = tool_registry.execute_tool(tool_name, parameters)
                        messages.append({
                            "role": "assistant",
                            "content": tool_response
                        })
                        return tool_response
                    except Exception as e:
                        return f"Error parsing function call: {e}"

        # Append the AI's response to the messages list
        local_messages.append({
            "role": "assistant",
            "content": model_reply
        })

        return model_reply
    except json.JSONDecodeError as e:
        return f"JSON decode error: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"
