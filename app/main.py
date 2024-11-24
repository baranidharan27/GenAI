# import streamlit as st
# from transformers import GPT2LMHeadModel, GPT2Tokenizer

# # Load pre-trained GPT-2 model and tokenizer
# model_name = "distilgpt2"
# model = GPT2LMHeadModel.from_pretrained(model_name)
# tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# # Function to generate content
# def generate_content(input_text):
#     inputs = tokenizer.encode(input_text, return_tensors="pt")
#     outputs = model.generate(inputs, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2)
#     generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
#     return generated_text

# # Streamlit UI Setup
# st.set_page_config(page_title="AI Content Generator", page_icon="🤖", layout="wide")

# # Sidebar
# st.sidebar.title("Settings")
# max_length = st.sidebar.slider("Maximum Length", min_value=50, max_value=200, value=100, step=10)
# no_repeat_ngram_size = st.sidebar.slider("No Repeat N-gram Size", min_value=1, max_value=5, value=2)
# theme_choice = st.sidebar.radio("Theme", options=["Light", "Dark"], index=0)

# if theme_choice == "Dark":
#     st.markdown(
#         """
#         <style>
#         body {
#             background-color: #1e1e1e;
#             color: white;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

# # Main UI
# st.title("Content Generator")
# st.subheader("Easily generate creative text content!")
# st.write("Enter a prompt below to see what AI can create for you.")

# # User Input
# user_input = st.text_input("Your Prompt:")
# if st.button("Generate"):
#     if user_input:
#         with st.spinner("Generating content..."):
#             response = generate_content(user_input)
#         st.success("Here's the generated content:")
#         st.write(response)
#     else:
#         st.warning("Please enter a prompt to generate content.")

# # Extra Options
# st.markdown("---")
# st.subheader("Additional Options")
# st.write("🔹 **Example Prompts:** Click below to use sample prompts.")
# examples = st.radio(
#     "Select an example prompt:",
#     options=["Write a short story about AI", "Explain the importance of education", "What is the future of technology?"],
#     index=0,
# )

# if st.button("Use Example"):
#     user_input = examples
#     st.experimental_rerun()

# st.write("🔹 **Feedback Form:** Let us know your thoughts!")
# feedback = st.text_area("Share your feedback:")
# if st.button("Submit Feedback"):
#     if feedback:
#         st.success("Thank you for your feedback!")
#     else:
#         st.warning("Please write your feedback before submitting.")


import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
model_name = "distilgpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Function to generate content
def generate_content(input_text):
    """
    Generate text content based on the given input prompt.

    Args:
        input_text (str): User input or prompt for content generation.

    Returns:
        str: AI-generated content as a string.
    """
    inputs = tokenizer.encode(input_text, return_tensors="pt")
    outputs = model.generate(inputs, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text

# Streamlit UI Setup
st.set_page_config(page_title="AI Content Generator", page_icon="🤖", layout="wide")

# Sidebar
st.sidebar.title("Settings")
max_length = st.sidebar.slider("Maximum Length", min_value=50, max_value=200, value=100, step=10)
no_repeat_ngram_size = st.sidebar.slider("No Repeat N-gram Size", min_value=1, max_value=5, value=2)
theme_choice = st.sidebar.radio("Theme", options=["Light", "Dark"], index=0)

if theme_choice == "Dark":
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

# Main UI
st.title(" AI Content Generator")
st.subheader("Easily generate creative text content!")
st.write("Enter a prompt below to see what AI can create for you.")

# User Input
user_input = st.text_input("Your Prompt:")
if st.button("Generate"):
    if user_input:
        with st.spinner("Generating content..."):
            response = generate_content(user_input)
        st.success("Here's the generated content:")
        st.write(response)
    else:
        st.warning("Please enter a prompt to generate content.")

# Extra Options
st.markdown("---")
st.subheader("Additional Options")
st.write("🔹 **Example Prompts:** Click below to use sample prompts.")
examples = st.radio(
    "Select an example prompt:",
    options=["Write a short story about AI", "Explain the importance of education", "What is the future of technology?"],
    index=0,
)

if st.button("Use Example"):
    user_input = examples
    st.experimental_rerun()

st.write("🔹 **Feedback Form:** Let us know your thoughts!")
feedback = st.text_area("Share your feedback:")
if st.button("Submit Feedback"):
    if feedback:
        st.success("Thank you for your feedback!")
    else:
        st.warning("Please write your feedback before submitting.")
