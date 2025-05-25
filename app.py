import streamlit as st
import pytesseract
from PIL import Image
from pdf2image import convert_from_bytes
import pdfplumber
import os
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()

# Initialize OpenAI client
openai.api_key = "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"

def extract_text_from_image(image):
    """Extract text from an image using OCR"""
    text = pytesseract.image_to_string(image)
    return text

def extract_text_from_pdf(pdf_bytes):
    """Extract text from PDF using pdfplumber"""
    text = ""
    with pdfplumber.open(pdf_bytes) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def analyze_report(text):
    """Analyze the medical report using OpenAI API"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a medical report analyzer. Analyze the given medical report and provide key findings, diagnosis, and recommendations."},
                {"role": "user", "content": f"Please analyze the following medical report:\n{text}"}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error analyzing report: {str(e)}"

def main():
    st.title("Medical Reports Analyzer")
    
    uploaded_file = st.file_uploader("Upload Medical Report", type=['jpg', 'jpeg', 'png', 'pdf'])
    
    if uploaded_file is not None:
        file_type = uploaded_file.type
        
        if file_type.startswith('image/'):
            # Handle image files
            image = Image.open(uploaded_file)
            text = extract_text_from_image(image)
        elif file_type == 'application/pdf':
            # Handle PDF files
            text = extract_text_from_pdf(uploaded_file.getvalue())
        else:
            st.error("Unsupported file type. Please upload JPG, PNG, or PDF files.")
            return
        
        # Display extracted text
        st.subheader("Extracted Text")
        st.text_area("", text, height=300)
        
        # Analyze the report
        if st.button("Analyze Report"):
            with st.spinner("Analyzing report..."):
                analysis = analyze_report(text)
                st.subheader("Analysis Results")
                st.write(analysis)

if __name__ == "__main__":
    main()
