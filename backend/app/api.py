# # backend/app/api.py
# from fastapi import APIRouter
# from pydantic import BaseModel
# from backend.src.models.llm_model import LLMModel

# from backend.src.config.settings import ModelConfig

# router = APIRouter()

# # Initialize model
# model_config = ModelConfig()
# model = LLMModel(model_config)

# # Create a data model for incoming user messages
# class Message(BaseModel):
#     text: str

# # API route to handle chat messages
# @router.post("/api/chat")
# async def chat(message: Message):
#     user_message = message.text
#     # Use the model to generate the response
#     model_response = model.generate(user_message)
#     return {"response": model_response}
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.src.models.llm_model import LLMModel
from backend.src.config.settings import ModelConfig
from backend.src.utils.prompt_templates import PromptTemplates

router = APIRouter()

# Initialize model
model_config = ModelConfig()
model = LLMModel(model_config)

class Message(BaseModel):
    text: str

@router.post("/api/chat", response_model=dict)
async def chat(message: Message):
    try:
        user_message = message.text
        model_response = model.generate(user_message)
        return {"response": model_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health")
async def health_check():
    return {"status": "ok"}        
        