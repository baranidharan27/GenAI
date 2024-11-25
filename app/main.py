# import streamlit as st
# from transformers import AutoTokenizer, AutoModelForCausalLM

# # Load GPT-2 tokenizer and model
# tokenizer = AutoTokenizer.from_pretrained("gpt2")
# model = AutoModelForCausalLM.from_pretrained("gpt2")


# def generate_content(input_text, max_length):
#     inputs = tokenizer.encode(input_text, return_tensors="pt")
#     outputs = model.generate(
#         inputs, max_length=max_length, num_return_sequences=1, no_repeat_ngram_size=2
#     )
#     generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
#     return generated_text


# # Streamlit UI Setup
# st.set_page_config(page_title="Content Generator", page_icon="", layout="wide")

# # Sidebar
# st.sidebar.title("Settings")
# max_length = st.sidebar.slider("Maximum Length", min_value=50, max_value=200, value=100, step=10)
# no_repeat_ngram_size = st.sidebar.slider("No Repeat N-gram Size", min_value=1, max_value=5, value=2)

# # Main UI
# st.title(" Content Generator")
# st.subheader("creative text content!")
# st.write("Enter a prompt below to see what can create for you.")

# # User Input
# if "user_input" not in st.session_state:
#     st.session_state["user_input"] = ""

# user_input = st.text_input("Your Prompt:", st.session_state["user_input"])
# if st.button("Generate"):
#     if user_input:
#         with st.spinner("Generating content..."):
#             response = generate_content(user_input, max_length)
#         st.success("Here's the generated content:")
#         st.write(response)
#     else:
#         st.warning("Please enter a prompt to generate content.")

# # Example Prompts
# examples = st.radio(
#     "Select an example prompt:",
#     ["Write a short story about AI", "Explain the importance of education", "What is the future of technology?"],
#     index=0,
# )

# if st.button("Use Example"):
#     st.session_state["user_input"] = examples
#     st.experimental_set_query_params(prompt=examples)
#     st.experimental_rerun()

# # Feedback
# st.write("🔹 **Feedback Form:** Let us know your thoughts!")
# feedback = st.text_area("Share your feedback:")
# if st.button("Submit Feedback"):
#     if feedback:
#         st.success("Thank you for your feedback!")
#     else:
#         st.warning("Please write your feedback before submitting.")


import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load GPT-2 tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")

# Structured prompt to focus strictly on answering the question
structured_prompt = """
You are an AI assistant tasked with answering user questions clearly and concisely.
Answer only the question asked. Provide factual, direct, and precise information, with no elaboration beyond the query.
If the question is unclear, say: "I don't know the answer to that."
Do not invent information or make assumptions. Avoid any creative or speculative responses.

Question: {input_text}
Answer:
"""

# Function to generate content
def generate_content(input_text):
    """
    Generate text content based on the given input prompt.

    Args:
        input_text (str): User input or prompt for content generation.

    Returns:
        str: AI-generated content as a string.
    """
    # Combine the structured prompt with user input
    full_prompt = structured_prompt.format(input_text=input_text)

    # Tokenize input and generate response
    inputs = tokenizer.encode(full_prompt, return_tensors="pt")
    outputs = model.generate(
        inputs, 
        max_length=512, 
        top_k=50,               # Control randomness by considering the top 50 tokens
        temperature=0.2,        # Keep responses factual and to the point
        top_p=0.95,             # Ensure diversity but within controlled bounds
        num_return_sequences=1, 
        no_repeat_ngram_size=2  # Avoid repetition
    )

    # Decode the generated text and return the response
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Extract just the answer from the generated output (after "Answer:" label)
    response_start = generated_text.find("Answer:") + len("Answer: ")
    response = generated_text[response_start:].strip()
    
    return response

# Streamlit UI Setup
st.set_page_config(page_title="Content Generator", page_icon="", layout="wide")

# Sidebar
st.sidebar.title("Settings")
max_length = st.sidebar.slider("Maximum Length", min_value=50, max_value=512, value=100, step=10)
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
st.title(" Content Generator")
st.subheader("Easily generate factual answers to your questions!")
st.write("Enter a query below to get a direct and concise response.")

# User Input
user_input = st.text_input("Your Question:")

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
    options=["What is a volcano?", "What is the capital of France?", "Explain Newton's Laws of Motion."],
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