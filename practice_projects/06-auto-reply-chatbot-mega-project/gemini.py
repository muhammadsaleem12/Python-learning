import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def ask_ai(prompt):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        config={
            "system_instruction": "You are a real person named Chris who speaks english. you're from California and is a coder. You analyze chat history and repond like Chris. give shorter replies not paragraphs"
        },
        contents=prompt
    )

    return response.text