from fastapi import FastAPI
from pydantic import BaseModel
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Initialize FastAPI app
app = FastAPI()

# Load GPT-2 model and tokenizer
model_name = "distilgpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Request schema
class ChatRequest(BaseModel):
    prompt: str
    max_length: int = 100
    no_repeat_ngram_size: int = 2

# Endpoint for content generation
@app.post("/generate/")
def generate_response(request: ChatRequest):
    inputs = tokenizer.encode(request.prompt, return_tensors="pt")
    outputs = model.generate(
        inputs, 
        max_length=request.max_length, 
        num_return_sequences=1, 
        no_repeat_ngram_size=request.no_repeat_ngram_size
    )
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": generated_text}
