# CrawlerAI Chatbot

A RAG-based chatbot that allows you to extract information from websites, generate summaries, and interact with the content using LLMs.

## Features

- 🌐 **Website Extraction**: Crawl and extract content from any webpage using URLs
- 📝 **Smart Summarization**: Generate concise summaries of extracted content
- 💬 **Interactive Chat**: Ask questions about the content using a powerful LLM
- 🔍 **RAG Architecture**: Utilizes embeddings and FAISS vector store for efficient retrieval
- 🚀 **Streamlit Interface**: User-friendly web interface

## Prerequisites

- Python 3.12+
- OpenAI API key
- Docker (optional)

## Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd "Chat with Site"
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up environment variables by creating a `.env` file:

```properties
OPENAI_API_KEY=your_openai_api_key
```

## Running the Application

### Local Development

```bash
streamlit run app.py
```

### Using Docker

```bash
docker build -t crawlerai .
docker run -p 8501:8501 crawlerai
```

Visit `http://localhost:8501` in your browser.

## Usage

1. Select "AI Engine" from the sidebar
2. Enter a URL to crawl
3. Wait for the extraction to complete
4. Generate a summary (optional)
5. Create embeddings for the extracted content
6. Start chatting with the AI about the webpage content

## Project Structure

```
Chat with Site/
├── app.py              # Main Streamlit application
├── config.py           # Configuration settings
├── requirements.txt    # Project dependencies
├── Dockerfile         # Docker configuration
└── .env              # Environment variables
```

## Contributing

Feel free to open issues and submit pull requests.

## License

MIT License
