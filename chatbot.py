

import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")


# Use the correct Gemini API version
genai.configure(api_key=api_key)


# Use the preview GenerativeModel class
model = genai.GenerativeModel("models/gemini-1.5-pro-001")


def ask_chatbot(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"
