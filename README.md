# Medical Reports Analyzer

A web application that analyzes medical reports using OCR and AI. It supports JPG, PNG, and PDF files.

## Features

- Upload medical reports in JPG, PNG, or PDF format
- Extract text using OCR
- Analyze reports using OpenAI's GPT-3.5
- Get key findings, diagnosis, and recommendations

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
streamlit run app.py
```

3. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501)

## Deploying to Netlify

1. Create a `netlify.toml` file with:
```toml
[build]
  command = "pip install -r requirements.txt && streamlit run app.py"
  publish = "dist"

[build.environment]
  PYTHONPATH = "."
```

2. Push your code to GitHub

3. Create a new site on Netlify

4. Connect your GitHub repository

5. Deploy the site

## Note

Make sure to keep your OpenAI API key secure and never commit it to version control.
