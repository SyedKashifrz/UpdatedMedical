# Medical Report Analyzer

A Streamlit app to analyze medical reports using OCR and Gemini AI.

## Features

- Upload PDFs and JPGs.
- Extract text using OCR (Tesseract).
- Analyze reports using Gemini Pro (Google AI).
- Simple explanations for medical terms.

## Setup

1. Clone the repo.
2. Create `.env` with your Google API key.
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the app:
   ```
   streamlit run app.py
   ```

## Deployment

Use [Streamlit Cloud](https://streamlit.io/cloud) to deploy.
Netlify does **not support** Python backend apps.
