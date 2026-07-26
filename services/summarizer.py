from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_summary(text):

    prompt = f"""
    You are an enterprise document analyst.

    Analyze this document and provide:

    1. A concise summary (5 bullet points)
    2. Document type
    3. Key skills
    4. Technologies mentioned

    Return plain text only.

    Document:

    {text}
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    return response.text