import asyncio
from crawl4ai import AsyncWebCrawler, CacheMode, CrawlerRunConfig
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from config import LLM_CONFIG

async def extract_from_url(url):
    crawler_run_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url, config=crawler_run_config)
        return result.markdown

def generate_summary(content):
    summary_prompt_template = """
    You are an AI assistant that is tasked with summarizing a web page.
    Your summary should be detailed and cover all key points mentioned in the content. 
    Below is the content of the web page:
    {content}

    please provide a comprehensive and detailed summary in markdown format.
    """
    summary_prompt = PromptTemplate(template=summary_prompt_template, input_variables=['content'])
    prompt_text = summary_prompt.format(content=content)
    
    summarizer = ChatOpenAI(
        model_name=LLM_CONFIG["model_name"],
        temperature=0.2,
        max_tokens=1500
    )
    return summarizer(prompt_text).content
