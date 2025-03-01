from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from config import LLM_CONFIG, CHAT_HISTORY_PATH

def setup_qa_chain(vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    
    prompt_template = """
    You are an AI assistant tasked with answering questions based solely
    on the provided context. Your goal is to generate a comprehensive answer
    for the given question using only the information available in the context.

    context: {context}

    question: {question}

    <response> Your answer in Markdown format. </response>
    """
    prompt = PromptTemplate(template=prompt_template, input_variables=['context', 'question'])
    
    llm = ChatOpenAI(**LLM_CONFIG)
    
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt},
        verbose=True
    )

def save_chat_history(chat_history):
    chat_file_content = "\n\n".join(
        [f"User: {chat['user']}\nBot: {chat['bot']}" for chat in chat_history]
    )
    with open(CHAT_HISTORY_PATH, "w", encoding="utf-8") as cf:
        cf.write(chat_file_content)
