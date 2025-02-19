# # src/utils/prompt_templates.py

# class PromptTemplates:
#     @staticmethod
#     def create_expert_prompt(question: str) -> str:
#         return f"""You are a helpful AI assistant. Answer the following question clearly and accurately in a few sentences.
# If you don't know something, simply say you don't know.

# Question: {question}
# Answer: Let me explain this clearly.
# """

#     @staticmethod
#     def extract_response(generated_text: str) -> str:
#         # Find the answer part after "Let me explain this clearly."
#         marker = "Let me explain this clearly."
#         start_idx = generated_text.find(marker)
#         if start_idx != -1:
#             return generated_text[start_idx + len(marker):].strip()
#         return generated_text.strip()

# # src/config/settings.py
# from dataclasses import dataclass

# @dataclass
# class ModelConfig:
#     model_name: str = "gpt2"
#     max_length: int = 150  # Shorter responses
#     temperature: float = 0.5  # More focused
#     top_p: float = 0.85
#     top_k: int = 40
#     num_return_sequences: int = 1
#     no_repeat_ngram_size: int = 3
#     length_penalty: float = 1.2  # Encourage completeness
#     repetition_penalty: float = 1.3  # Strongly discourage repetition

# # src/models/llm_model.py
# class LLMModel:
#     def __init__(self, config: ModelConfig):
#         self.config = config
#         self.tokenizer = AutoTokenizer.from_pretrained(config.model_name)
#         self.model = AutoModelForCausalLM.from_pretrained(config.model_name)
    
#     def generate(self, prompt: str) -> str:
#         try:
#             inputs = self.tokenizer.encode(prompt, return_tensors="pt", max_length=self.config.max_length, truncation=True)
#             outputs = self.model.generate(
#                 inputs,
#                 max_length=self.config.max_length,
#                 temperature=self.config.temperature,
#                 top_p=self.config.top_p,
#                 top_k=self.config.top_k,
#                 num_return_sequences=self.config.num_return_sequences,
#                 no_repeat_ngram_size=self.config.no_repeat_ngram_size,
#                 length_penalty=self.config.length_penalty,
#                 repetition_penalty=self.config.repetition_penalty,
#                 pad_token_id=self.tokenizer.eos_token_id,
#                 early_stopping=True
#             )
#             return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
#         except Exception as e:
#             return f"I apologize, but I encountered an error. Could you please rephrase your question?"


class PromptTemplates:
    @staticmethod
#     def create_prompt(question: str) -> str:
#         return f"""Instruct: Provide a clear and accurate answer to the following question. Be informative but concise.

# Question: {question}

# Answer: Let me provide a clear explanation."""


    def create_prompt(question: str) -> str:
            return f""" You are a multi-domain expert. A user has given you the following question:

        Things to Do:
        1. Reformulate the question with proper grammar and punctuation, and correct any spelling mistakes.
        2. Understand the user's intent, background, and knowledge level. Consider those factors while formulating your answer.

        Your Role:
        1. Identify the domain of the question. Assume you are an expert in the relevant domain. 
        2. For example, if the question is about "What is a Transformer?" assume it is about the domain of "Machine Learning".

        Answering Instructions:
        1. Provide a clear, concise, and well-organized response.
        2. Avoid hallucinations or false information.
        3. Think step by step before answering, and if applicable, use Chain of Thought reasoning.
        4. If needed, include mathematical or coding-based responses.
        5. Provide references if applicable.

        The Question:
        {question}

        The Answer:"""

    @staticmethod
    def extract_response(generated_text: str) -> str:
        # Find the answer part after the marker
        marker = "Answer:"
        start_idx = generated_text.find(marker)
        if start_idx != -1:
            return generated_text[start_idx + len(marker):].strip()
        return generated_text.strip()