from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mistralai import ChatMistralAI

from backend.config.settings import settings

# setup llms

# Groq
groq_llm = ChatGroq(model=settings.groq_model_name,
               temperature=settings.temperature,
               api_key=settings.groq_api_key
               )

# Mistral
gemini_llm = ChatMistralAI(model=settings.mistral_model_name,
               temperature=settings.temperature,
               api_key=settings.mistral_api_key
               )

# Gemini
mistral_llm = ChatGoogleGenerativeAI(model=settings.gemini_model_name,
               temperature=settings.temperature,
               api_key=settings.gemini_api_key
               )


response = gemini_llm.invoke("Hello!")
print(response.content)
