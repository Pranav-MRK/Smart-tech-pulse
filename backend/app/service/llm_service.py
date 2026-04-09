import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# Initialize LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name=os.getenv("GROQ_MODEL_NAME", "llama-3.1-8b-instant")
)

def generate_summary(news_list, interests):
    # Combine news into text
    news_text = ""
    
    for news in news_list[:5]:
        news_text += f"Title: {news['title']}\nSummary: {news['summary']}\n\n"

    prompt = f"""
    You are an AI news assistant.

    User interests: {interests}

    Based on the following news, generate:
    1. Short summary
    2. Why it matters

    News:
    {news_text}
    """

    response = llm.invoke(prompt)

    return response.content