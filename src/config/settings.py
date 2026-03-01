import os
from typing import Literal, Optional, Any
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
import yaml

class Settings(BaseSettings):
    # load variables from .env file
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    AI_GATEWAY = Field(...)
    AI_GATEWAY_KEY = Field(...)
    GOOGLE_PLACES_API_KEY = Field(...)
    TAVILY_API_KEY = Field(...)
    OPEN_WEATHER_API_KEY = Field(...)
    EXCHANGE_RATE_API_KEY = Field(...)
    FOURSQUARE_PLACES_API_KEY = Field(...)
    SUPABASE_DB_URL: str = Field(...)
    EXCHANGE_RATE_API: str = Field(...)

    def load_model_config(self, config_path: str = "model_config.yaml") -> dict:
        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file) # load the YAML file and parse it into a Python dictionary
        return self.config
    
    def __getitem__(self, key):
        return self.config[key]