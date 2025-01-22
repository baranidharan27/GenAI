# from dataclasses import dataclass


# @dataclass
# class ModelConfig:
#     model_name: str = "mistralai/Mistral-7B-Instruct-v0.1"
#     max_length: int = 512
#     temperature: float = 0.7
#     top_p: float = 0.9
#     top_k: int = 50
#     num_return_sequences: int = 1
#     no_repeat_ngram_size: int = 3
#     length_penalty: float = 1.0
#     repetition_penalty: float = 1.1
#     device: str = "cuda"  

# @dataclass
# class UIConfig:
#     page_title: str = "Content Generator"
#     page_icon: str = ""
#     layout: str = "wide"
#     min_length: int = 50
#     max_length: int = 512
#     default_length: int = 100
#     length_step: int = 10


# src/config/settings.py
from dataclasses import dataclass

@dataclass
class ModelConfig:
    model_name: str = "microsoft/phi-2"
    max_length: int = 512
    temperature: float = 0.7
    top_p: float = 0.9
    top_k: int = 40
    num_return_sequences: int = 1
    no_repeat_ngram_size: int = 3
    length_penalty: float = 1.0
    repetition_penalty: float = 1.1
    device: str = "cpu"

@dataclass
class UIConfig:
    # Page settings
    page_title: str = "Content Generator"
    page_icon: str = ""
    layout: str = "wide"
    
    # Sidebar settings
    min_length: int = 50
    max_length: int = 512
    default_length: int = 100
    length_step: int = 10
    
    # Theme settings
    default_theme: str = "Light"
    available_themes: tuple = ("Light", "Dark")
    
    # Example prompts
    default_examples: tuple = (
        ""
    )