# Azure OpenAI Interactive PDF Reader

The PDF Reader AI Agent is an advanced conversational assistant designed to help users interact with and extract information from PDF documents. Utilizing the power of generative AI (GenAI), this agent can process multiple PDFs, answer user queries based on the contents of the documents. It's designed to be user friendly and is built with a streamlined interface using Streamlit.

![Demo image](https://github.com/abhisheksimion/azure-openai-interactive-pdf-reader/blob/main/app_screenshot.png)

## Features

- Multiple PDF Support: Upload and process multiple PDF files simultaneously.
- Interactive Chat Interface: Engage in a conversation with the AI to ask questions about the content of the uploaded PDFs.
- Context Preservation: Maintains chat history to provide coherent and context-aware responses.
- Streamlined UI: User friendly interface built with Streamlit, including dynamic content display and CSS styling.

## Prerequisites

- Python 3.8+
- Streamlit
- PyPDF2
- OpenAI API Key, API endpoint, API version and model name
- Other required Python libraries specified in requirements.txt


## Setup Instructions

1. **Clone the Repository**
   ```bash
    git clone https://github.com/abhisheksimion/azure-openai-interactive-pdf-reader.git
    cd azure-openai-interactive-pdf-reader

   ```
   
2. **Create and Activate a Virtual Environment**
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Setup your OpenAI**
   - Create a .env file in the root directory of the project and add your OpenAI API details
    ```bash
   AZURE_ENDPOINT=your_openai_api_endpoint
   AZURE_API_KEY=your_openai_api_key
   AZURE_API_VERSION=your_openai_api_version
   MODEL_NAME=your_openai_model_name
    ```
6. **Running using streamlit**
   ```bash
   streamlit run app.py
   ```

Reference PDF (for upload): https://web.pdx.edu/~arhodes/ai5.pdf
