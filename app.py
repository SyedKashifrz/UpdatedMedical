import streamlit as st
from PIL import Image
import fitz  # PyMuPDF
import io
import os
import google.generativeai as genai
from dotenv import load_dotenv
import easyocr
import numpy as np

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("Missing GOOGLE_API_KEY. Please add it to the .env file.")
    st.stop()

genai.configure(api_key=api_key)
reader = easyocr.Reader(['en'], gpu=False)

def extract_text_from_image(img):
    try:
        result = reader.readtext(np.array(img), detail=0)
        return " ".join(result)
    except Exception as e:
        return f"Error extracting text from image: {str(e)}"

def extract_text_from_pdf(file):
    try:
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        return f"Error extracting text from PDF: {str(e)}"

def analyze_text(text):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(
            f"You are a medical report analyzer. Please explain this medical report in simple language:\n\n{text}"
        )
        return response.text
    except Exception as e:
        return f"Error analyzing report: {str(e)}"

def main():
    st.title("🧾 Medical Report Analyzer")
    st.write("Upload your medical report (PDF or JPG) to get a simple explanation.")

    uploaded_file = st.file_uploader("Upload Report", type=["pdf", "jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.success("File uploaded successfully.")
        with st.spinner("Extracting text..."):
            if uploaded_file.type == "application/pdf":
                text = extract_text_from_pdf(uploaded_file)
            else:
                img = Image.open(uploaded_file)
                text = extract_text_from_image(img)

        if not text or text.strip() == "":
            st.error("No text could be extracted.")
            return

        st.subheader("📝 Extracted Text Preview")
        st.text_area("Text", text[:1000] + "..." if len(text) > 1000 else text, height=200)

        if st.button("Analyze Report"):
            with st.spinner("Analyzing report..."):
                result = analyze_text(text)
            st.subheader("📊 Analysis")
            st.write(result)

if __name__ == "__main__":
    main()
