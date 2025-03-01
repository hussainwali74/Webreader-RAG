import streamlit as st

def initialize_session_state():
    if "url_submitted" not in st.session_state:
        st.session_state.url_submitted = False
    if "extraction_done" not in st.session_state:
        st.session_state.extraction_done = False
    if "extraction_text" not in st.session_state:
        st.session_state.extraction_text = ""
    if "embedding_done" not in st.session_state:
        st.session_state.embedding_done = False
    if "vectorestore" not in st.session_state:
        st.session_state.vectorestore = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "summary" not in st.session_state:
        st.session_state.summary = ""

def reset_state():
    st.session_state.extraction_done = False
    st.session_state.embedding_done = False
    st.session_state.chat_history = []
    st.session_state.summary = ""
    st.session_state.extraction_text = ""
    st.session_state.vectorestore = None
