# from src.config.settings import ModelConfig, UIConfig
# from src.models.llm_model import LLMModel
# from src.utils.prompt_templates import PromptTemplates
# from src.ui.components import UIComponents
# import streamlit as st

# def main():
#     # Initialize configurations
#     model_config = ModelConfig()
#     ui_config = UIConfig()
    
#     # Initialize model
#     model = LLMModel(model_config)
    
#     # Setup UI
#     UIComponents.setup_page_config(
#         ui_config.page_title,
#         ui_config.page_icon,
#         ui_config.layout
#     )
    
#     # Create sidebar
#     max_length, theme = UIComponents.create_sidebar(ui_config)
    
#     # Create main content
#     user_input = UIComponents.create_main_content()
    
#     # Handle generation
#     if st.button("Generate"):
#         if user_input:
#             with st.spinner("Generating content..."):
#                 prompt = PromptTemplates.create_expert_prompt(user_input)
#                 response = model.generate(prompt)
#                 final_response = PromptTemplates.extract_response(response)
#             st.success("Here's the generated content:")
#             st.write(final_response)
#         else:
#             st.warning("Please enter a prompt to generate content.")
    
#     # Show examples
#     examples = [
#         "What is a volcano?",
#         "What is the capital of France?",
#         "Explain Newton's Laws of Motion."
#     ]
#     UIComponents.show_examples(examples, lambda x: st.session_state.update({"user_input": x}))
    
#     # Feedback form
#     st.write("🔹 **Feedback Form:** Let us know your thoughts!")
#     feedback = st.text_area("Share your feedback:")
#     if st.button("Submit Feedback"):
#         if feedback:
#             st.success("Thank you for your feedback!")
#         else:
#             st.warning("Please write your feedback before submitting.")

# if __name__ == "__main__":
#     main()


# src/main.py
import streamlit as st
from src.config.settings import ModelConfig, UIConfig
from src.models.llm_model import LLMModel
from src.utils.prompt_templates import PromptTemplates
from src.ui.components import UIComponents

def main():
    # Initialize configurations
    model_config = ModelConfig()
    ui_config = UIConfig()
    
    # Initialize model
    model = LLMModel(model_config)
    
    # Setup UI
    UIComponents.setup_page_config(ui_config)
    
    # Create sidebar
    max_length, theme = UIComponents.create_sidebar(ui_config)
    
    # Apply theme
    if theme == "Dark":
        st.markdown(
            """
            <style>
            body {
                background-color: #1e1e1e;
                color: white;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
    
    # Create main content
    user_input = UIComponents.create_main_content()
    
    # Handle generation
    if st.button("Generate"):
        if user_input:
            with st.spinner("Generating content..."):
                prompt = PromptTemplates.create_prompt(user_input)
                response = model.generate(prompt)
                final_response = PromptTemplates.extract_response(response)
            st.success("Here's the generated content:")
            st.write(final_response)
        else:
            st.warning("Please enter a prompt to generate content.")
    
    # Show examples
    UIComponents.show_examples(
        ui_config,
        lambda x: st.session_state.update({"user_input": x})
    )
    
    # Feedback form
    st.write("🔹 **Feedback Form:** Let us know your thoughts!")
    feedback = st.text_area("Share your feedback:")
    if st.button("Submit Feedback"):
        if feedback:
            st.success("Thank you for your feedback!")
        else:
            st.warning("Please write your feedback before submitting.")