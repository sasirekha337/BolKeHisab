from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    database_url: str = "sqlite:///./bolkehisab.db"
    secret_key: str = "dev-secret-change-me"
    use_mock_stt: bool = True
    use_mock_vision: bool = True
    use_mock_llm: bool = True
    razorpay_key_id: str = ""
    razorpay_key_secret: str = ""

    class Config:
        env_file = ".env"
        extra = "ignore"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
