from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from config import EMBEDDING_CONFIG, FAISS_INDEX_PATH, OUTPUT_MD_PATH

def create_embeddings(content):
    # Save content to markdown file
    with open(OUTPUT_MD_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    
    # Load and process the content
    loader = UnstructuredMarkdownLoader(OUTPUT_MD_PATH)
    data = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=EMBEDDING_CONFIG["chunk_size"],
        chunk_overlap=EMBEDDING_CONFIG["chunk_overlap"]
    )
    texts = text_splitter.split_documents(data)
    
    # Create embeddings
    embeddings = OpenAIEmbeddings(model=EMBEDDING_CONFIG["model"])
    vectorstore = FAISS.from_documents(texts, embeddings)
    
    # Save vector store
    vectorstore.save_local(FAISS_INDEX_PATH)
    
    return vectorstore
