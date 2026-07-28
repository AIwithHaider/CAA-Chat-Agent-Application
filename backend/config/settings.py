from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    groq_api_key: str
    model_name: str
    temperature: float
    tavily_api_key: str
    glm_api_key: str
    openai_api_key: str

    model_config = SettingsConfigDict(
        env_file= ".env",
        env_file_encoding= "utf-8"
    )

settings = Settings()



