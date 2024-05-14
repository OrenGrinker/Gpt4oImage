import os
import streamlit as st
from openai import OpenAI
import base64
from utils import get_image_description

# Streamlit app layout
st.title("Image Description using GPT-4o")
st.write("Upload an image and get a description using GPT-4o.")

# Textbox for updating OpenAI API key
api_key = st.text_input("Enter your OpenAI API key", type="password")
if not api_key:
    api_key = os.environ.get("OPENAI_API_KEY", "")

if api_key:
    # Initialize the OpenAI client
    client = OpenAI(api_key=api_key)

    # Textbox for updating the prompt
    prompt = st.text_input("Enter the prompt for image description", "What’s in this image?")

    # Upload image button
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        try:
            # Display the uploaded image
            st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
            st.write("")
            st.write("Classifying...")

            # Get the image description
            description = get_image_description(client, uploaded_file, prompt)
            st.write(description)
        except Exception as e:
            st.error(f"Error: {e}")
else:
    st.error("Please provide a valid OpenAI API key.")
