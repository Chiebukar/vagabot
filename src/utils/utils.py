import os
from dotenv import load_dotenv
from typing import Literal, Optional, Any
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
import yaml
from src.config.settings import Settings
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI


class ModelLoader:
    def __init__(self, config_loader):
        self.config_loader = config_loader

    def load_model(self, provider):
        llm_config = self.config_loader.get_llm_config(provider)
        if not llm_config:
            raise ValueError(f"No configuration found for provider: {provider}")
        
        # Here you would add logic to initialize and return the model based on the configuration
        # For example, if using OpenAI's API:
        if llm_config['provider'] == 'openai':
            from openai import OpenAI
            return OpenAI(model=llm_config['model'], temperature=llm_config['temperature'])
        
        # Add logic for other providers as needed
        raise NotImplementedError(f"Model loading for provider {provider} is not implemented yet.")
    

class Settings(BaseModel):
    llm_provider: Literal['openai', 'groq'] = Field(..., description="The LLM provider to use.")
    config_path: str = Field(..., description="Path to the configuration file.")

    def __post_init__(self):
        self.config = load_config(self.config_path)