from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class GenerationModelName(str, Enum):
    """Model names for text generation"""
    # API models
    GEMINI_2_FLASH = "gemini-2.0-flash"

    # Huggingface models
    LLAMA_3_1_8B = "meta-llama/Llama-3.1-8B-Instruct"
    GPT_2 = "openai-community/gpt2"
