from langchain_groq import ChatGroq
from app.config import GROQ_API_KEY


def get_llm():
    return ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=GROQ_API_KEY,
        temperature=0,
    )


