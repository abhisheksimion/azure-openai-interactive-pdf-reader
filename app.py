import streamlit as st
from main import ask_question, extract_text_from_pdf, get_system_prompt  # Import necessary functions
from htmlTemplates import css, bot_template, user_template
# from transformers import pipeline

# Initialize the summarization pipeline
# summarizer = pipeline("summarization")

# Apply CSS styles
st.markdown(css, unsafe_allow_html=True)

# Initialize session state for chat history and conversation
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'pdf_texts' not in st.session_state:
    st.session_state.pdf_texts = []
if 'conversation' not in st.session_state:
    st.session_state.conversation = None

# Function to process files (actual processing logic should replace the placeholder)
def process_files(pdf_files):
    pdf_texts = [extract_text_from_pdf(pdf) for pdf in pdf_files]
    st.session_state.pdf_texts = pdf_texts
    st.session_state.conversation = "Initialized conversation object"  # Placeholder for actual conversation chain
    return "Processing complete"

# Sidebar for PDF upload
st.sidebar.title("Upload PDF(s)")
uploaded_files = st.sidebar.file_uploader("Upload your PDF(s) here and click 'Process'", type="pdf", accept_multiple_files=True)

if uploaded_files:
    # if st.sidebar.button("Process"):
    with st.spinner("Processing"):
        process_message = process_files(uploaded_files)
        st.sidebar.success("Done processing. You may now ask a question.")
        st.sidebar.write(process_message)

# Main interface
st.title("Interactive PDF Reader AI Agent")

if st.session_state.pdf_texts:
    st.markdown("### PDF Content")
    for i, pdf_text in enumerate(st.session_state.pdf_texts):
        st.expander(f"Show PDF Text {i + 1}").markdown(pdf_text, unsafe_allow_html=True)

# Display chat messages from history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(user_template.replace("{{MSG}}", message["content"]), unsafe_allow_html=True)
    elif message["role"] == "assistant":
        st.markdown(bot_template.replace("{{MSG}}", message["content"]), unsafe_allow_html=True)

# Function to summarize text
def summarize_text(text):
    summary = []#summarizer(text, max_length=500, min_length=50, do_sample=False)
    return summary[0]['summary_text']

# Accept user input at the bottom of the screen
prompt = st.chat_input("Type your message here")

if prompt:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Combine all PDF texts and summarize if too long
    combined_pdf_text = "\n\n".join(st.session_state.pdf_texts)
    if len(combined_pdf_text) > 1000:  # Adjust the threshold as needed
        combined_pdf_text = combined_pdf_text
        #combined_pdf_text = summarize_text(combined_pdf_text)

    # Prepare messages for the assistant response
    messages = [
        {"role": "system", "content": get_system_prompt()},
        {"role": "user", "content": f"PDF text: {combined_pdf_text}"}
    ] + st.session_state.messages

    # Get the AI response
    response = ask_question(messages, prompt)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Rerun the app to display the new messages
    st.rerun()
