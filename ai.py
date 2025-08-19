from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv("API")


def construct_prompt(name, date, time, place, question=None):
    prompt = (
        f"You are an expert Indian astrologer who provides exact predictions about a persona and also provides insights and remedies for betterment "
        f"A user has provided the following birth details for an astrology reading:\n"
        f"Name: {name}\n"
        f"Date of birth: {date}\n"
        f"Time of birth: {time}\n"
        f"Place of birth: {place}\n\n"
    )
    if question:
        prompt += f"The user also asks: \"{question}\"\n"
    prompt += (
        "Please provide a detailed and personalized astrology analysis for this user, "
        "including their sun sign, strengths, challenges, and a short forecast.All this has to be done in Indian Astrology style "
        "If a question is asked, answer it using astrological knowledge."
    )
    return prompt

import httpx

async def get_ai_response(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=data, headers=headers)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print("Error calling AI API:", e)
        return "Sorry, there was a problem generating your astrology results."
