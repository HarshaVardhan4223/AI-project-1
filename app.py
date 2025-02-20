import streamlit as st
import cv2
import numpy as np
from PIL import Image
import google.generativeai as genai

# Initialize Gemini AI
genai.configure(api_key="AIzaSyCo0NQ8sCcJT2sh9YlyS80XxM34rBwAAlg")

def analyze_image(image):
    """Process image and get suggestions from Gemini AI."""
    model = genai.GenerativeModel("gemini-pro")  # Use the appropriate model
    response = model.generate_content("Analyze this skin condition and provide possible insights.")
    return response.text  # Extract text from the response

st.title("Skin Disease Detection")

# Camera input
image_file = st.camera_input("Take a picture")

# Upload image input
uploaded_file = st.file_uploader("Or upload an image", type=["jpg", "png", "jpeg"])

if image_file or uploaded_file:
    if image_file:
        image = Image.open(image_file)
    else:
        image = Image.open(uploaded_file)
    
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Get AI analysis
    with st.spinner("Analyzing..."):
        result = analyze_image(image)
    
    st.subheader("Analysis Result:")
    st.write(result)
