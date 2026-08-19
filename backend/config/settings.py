from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    # Groq
    groq_api_key: str
    
    
    # Gemini
    gemini_api_key: str

    # Mistral
    mistral_api_key: str

    temperature: float
    
    tavily_api_key: str

    model_config = SettingsConfigDict(
        env_file= ".env",
        env_file_encoding= "utf-8"
    )

settings = Settings()



