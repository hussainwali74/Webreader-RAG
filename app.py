import streamlit as st
import asyncio
import sys
from streamlit_chat import message as st_message

from state_manager import initialize_session_state, reset_state
from extractor import extract_from_url, generate_summary
from embedding_manager import create_embeddings
from chat_manager import setup_qa_chain, save_chat_history
from config import PAGE_CONFIG

# Set Windows event loop policy
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

# Initialize session state
initialize_session_state()

# Page Config
st.set_page_config(**PAGE_CONFIG)
st.title("WebReader RAG Chatbot")

# Main application logic
def main():
    page = st.sidebar.radio("Select Page", ["Home", "AI Engine", "About"])
    
    if page == "Home":
        show_home_page()
    elif page == "AI Engine":
        show_ai_engine()

def show_home_page():
    st.markdown("""
    ## Welcome to WebReader RAG Chatbot
    **WebReader RAG** is a cutting-edge RAG chatbot application that allows you to extract information from any website using URL, generate detailed summaryies, and interact
                with the content using LLMs.
    **Features:**
                
    - **Website extraction:** Crawl and extract web page content using URL.

    - **Summarization:** Generate detailed summaries of the extracted content.
    - **Chatbot:** Interact with the extracted content using LLMs.
    - **Embeddings & Retrieval RAG:** 
        -- Use openai embeddings, stored in FAISS vector store and retrieval RAG to answer questions.

    Get started by seleting the **AI Engine** page from the sidebar.
    """)

def show_ai_engine():
    # URL Input form
    with st.form("url_form"):
        url_input = st.text_input("Enter URL to crawl")
        if st.form_submit_button(label="Submit") and url_input:
            st.session_state.url_submitted = True
            reset_state()

    if st.session_state.url_submitted:
        col1, col2, col3 = st.columns(3)
        
        # Column 1: Extraction and Summarization
        with col1:
            handle_extraction(url_input)
        
        # Column 2: Embeddings
        with col2:
            handle_embeddings()
        
        # Column 3: Chat Interface
        with col3:
            handle_chat_interface()

def handle_extraction(url_input):
    st.header("1. Website Extraction")
    if not st.session_state.extraction_done:
        with st.spinner("Extracting website..."):
            extracted = asyncio.run(extract_from_url(url_input))
            st.session_state.extracted_text = extracted
            st.session_state.extraction_done = True
        st.success("Extraction complete!")
    
    # Show preview and handle summarization
    preview = "\n".join(
        [line for line in st.session_state.extracted_text.splitlines()][:5]
    )
    st.text_area("Extracted Text Preview", preview, height=150)

    # Save the full extracted text as a file and provide a download button
    st.download_button(
        label="Download the extracted text",
        data=st.session_state.extracted_text,
        file_name="extracted_text.txt",
        mime="text/plain"
    )

    st.markdown("----")
    st.subheader("Summarize web page")
    if st.button("Summarize web page", key="summarize_button"):
        with st.spinner("Summarizing..."):
            summary = generate_summary(st.session_state.extracted_text)
            st.session_state.summary = summary
        st.success("Summarization complete!")
    if st.session_state.summary:
        st.subheader("Summary:")
        st.markdown(st.session_state.summary, unsafe_allow_html=False)

def handle_embeddings():
    st.header('2. Create Embeddings')
    if st.session_state.extraction_done and not st.session_state.embedding_done:
        if st.button("Create embeddings"):
            with st.spinner("Creating embeddings..."):
                create_embeddings(st.session_state.extracted_text)
                st.session_state.embedding_done = True
            st.success("Index created")
    elif st.session_state.embedding_done:
        st.info("Embeddings have been created")

def handle_chat_interface():
    st.header("3. Chat with the webpage")
    if st.session_state.embedding_done:
        user_input = st.text_input("Your query", key="chat_input")
        if st.button("Send", key="send_button") and user_input:
            response = setup_qa_chain(user_input)
            bot_answer = response['result']
            st.session_state.chat_history.append({"user": user_input, "bot": bot_answer})

            # Save the chat history to a file
            save_chat_history(st.session_state.chat_history)
        
        # Display the conversation using streamlit chat component
        if st.session_state.chat_history:
            for chat in st.session_state.chat_history:
                st_message(chat['user'], is_user=True)
                st_message(chat['bot'], is_user=False, allow_html=True)
    else:
        st.info("Please create embeddings to activate the chat")

if __name__ == "__main__":
    main()
