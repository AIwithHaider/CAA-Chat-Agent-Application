from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mistralai import ChatMistralAI
from backend.config.settings import settings


def get_llm(provider: str, model: str):

    if provider=="Groq":
        return ChatGroq(
            model=model,
            temperature=settings.temperature,
            api_key=settings.groq_api_key
        )

    elif provider=="Google":
        return  ChatGoogleGenerativeAI(
            model=model,
            temperature=settings.temperature,
            api_key=settings.gemini_api_key
        )

    elif provider=="MISTRAL":
        return ChatMistralAI(
            model=model,
            temperature=settings.temperature,
            api_key=settings.mistral_api_key
        )

    else:
        raise ValueError(f"Unsupported provider: {provider}")
