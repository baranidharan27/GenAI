from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from src.config.settings import ModelConfig  # Add this import

class LLMModel:
    def __init__(self, config: ModelConfig):
        self.config = config
        self.device = torch.device(config.device if torch.cuda.is_available() else "cpu")
        print(f"Using device: {self.device}")
        
        self.tokenizer = AutoTokenizer.from_pretrained(
            config.model_name,
            trust_remote_code=True
        )
        self.model = AutoModelForCausalLM.from_pretrained(
            config.model_name,
            trust_remote_code=True,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
            device_map="auto"
        ).to(self.device)
        
    def generate(self, prompt: str) -> str:
        try:
            inputs = self.tokenizer.encode(
                prompt,
                return_tensors="pt",
                max_length=self.config.max_length,
                truncation=True
            ).to(self.device)
            
            outputs = self.model.generate(
                inputs,
                max_length=self.config.max_length,
                temperature=self.config.temperature,
                top_p=self.config.top_p,
                top_k=self.config.top_k,
                num_return_sequences=self.config.num_return_sequences,
                no_repeat_ngram_size=self.config.no_repeat_ngram_size,
                length_penalty=self.config.length_penalty,
                repetition_penalty=self.config.repetition_penalty,
                pad_token_id=self.tokenizer.eos_token_id,
                early_stopping=True
            )
            
            return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        except Exception as e:
            print(f"Error during generation: {str(e)}")
            return "I apologize, but I encountered an error. Please try again."