from langchain_groq import ChatGroq
from backend.config.settings import settings

# setup llm
llm = ChatGroq(model=settings.model_name,
               temperature=settings.temperature,
               api_key=settings.groq_api_key
               )