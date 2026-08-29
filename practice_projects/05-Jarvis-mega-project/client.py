import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def ask_ai(prompt):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        config={
            "system_instruction": "You are a virtual assistant named Jarvis skilled in explaining complex programming concepts with creative flair. Give short reponses."
        },
        contents=prompt
    )

    return response.text