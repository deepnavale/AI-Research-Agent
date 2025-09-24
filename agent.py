import os
import requests
from io import BytesIO
from pypdf import PdfReader
from trafilatura import extract
from dotenv import load_dotenv

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def get_web_content(url: str) -> str:
   
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  

        content_type = response.headers.get("content-type", "")

        if "application/pdf" in content_type:
            pdf_file = BytesIO(response.content)
            reader = PdfReader(pdf_file)
            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
            return text if text else "Could not extract text from PDF."

        elif "text/html" in content_type:
            extracted_text = extract(response.text)
            return extracted_text if extracted_text else "Could not extract main content from the webpage."

        return "Unsupported content type."

    except requests.exceptions.RequestException as e:
        return f"Error fetching URL: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def run_agent(query: str) -> str:
  
    search_tool = TavilySearchResults(max_results=3)
    llm = ChatOllama(model="llama3.1", temperature=0.2)

    try:
        search_results = search_tool.invoke(query)
    except Exception as e:
        return f"Search API failed: {e}. Please check your API key and network connection."

    if not search_results:
        return "No search results found for the query."

    extracted_contents = []
    source_links = []
    for result in search_results:
        url = result.get('url')
        if url:
            source_links.append(url)
            content = get_web_content(url)
            extracted_contents.append(f"--- CONTENT FROM {url} ---\n{content}\n--- END OF CONTENT ---")

    combined_context = "\n\n".join(extracted_contents)

    if not combined_context.strip():
        return "Could not extract any content from the found sources."

    prompt_template = ChatPromptTemplate.from_messages([
        ("system",
         "You are an expert research analyst. Your task is to generate a structured, easy-to-read report based on a user's query and the provided web content. "
         "The report should include: "
         "1. A concise summary of the findings. "
         "2. Key points or takeaways in bullet form. "
         "3. A list of the source URLs you used. "
         "Do not add any preamble or concluding remarks outside of this structure."),
        ("human",
         "Query: {query}\n\n"
         "Content from sources:\n{context}")
    ])

    chain = prompt_template | llm | StrOutputParser()

    report = chain.invoke({
        "query": query,
        "context": combined_context
    })

    return report