from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    # Groq
    groq_api_key: str
    groq_model_name: str
    
    
    # Gemini
    gemini_api_key: str
    gemini_model_name: str

    # Mistral
    mistral_api_key: str
    mistral_model_name: str

    temperature: float
    tavily_api_key: str
    glm_api_key: Optional[str] = None
    openai_api_key: Optional[str] = None


    model_config = SettingsConfigDict(
        env_file= ".env",
        env_file_encoding= "utf-8"
    )

settings = Settings()



