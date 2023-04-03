import os
import openai
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

class Singleton(type):
    """
    Singleton metaclass for ensuring only one instance of a class.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Call method for the singleton metaclass."""
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(
                *args, **kwargs)
        return cls._instances[cls]


class Config(metaclass=Singleton):
    """
    Configuration class to store the state of bools for different scripts access.
    """

    def __init__(self):
        """Initialize the configuration class."""
        self.continuous_mode = False
        self.speak_mode = False
        # TODO - make these models be self-contained, using langchain, so we can configure them once and call it good 
        self.fast_llm_model = os.getenv("FAST_LLM_MODEL", "gpt-3.5-turbo") 
        self.smart_llm_model = os.getenv("SMART_LLM_MODEL", "gpt-4")
        self.fast_token_limit = int(os.getenv("FAST_TOKEN_LIMIT", 4000))
        self.smart_token_limit = int(os.getenv("SMART_TOKEN_LIMIT", 8000))
        
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")

        # Initialize the OpenAI API client
        openai.api_key = self.openai_api_key


    def set_continuous_mode(self, value: bool):
        """Set the continuous mode value."""
        self.continuous_mode = value

    def set_speak_mode(self, value: bool):
        """Set the speak mode value."""
        self.speak_mode = value

    def set_fast_llm_model(self, value: str):
        self.fast_llm_model = value

    def set_smart_llm_model(self, value: str):
        self.smart_llm_model = value

    def set_fast_token_limit(self, value: int):
        self.fast_token_limit = value

    def set_smart_token_limit(self, value: int):
        self.smart_token_limit = value

    def set_openai_api_key(self, value: str):
        self.apiopenai_api_key_key = value
    
    def set_elevenlabs_api_key(self, value: str):
        self.elevenlabs_api_key = value


        
