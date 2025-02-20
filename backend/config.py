from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    LLM_MODEL_PATH: str = "models/mistral-7b-instruct-v0.2.Q3_K_S.gguf"
    LLM_N_THREADS: int = 8
    LLM_N_GPU_LAYERS: int = -1
    LLM_CONTEXT_SIZE: int = 2048
    LLM_USE_METAL: bool = True
    
    class Config:
        env_file = ".env"

settings = Settings() 