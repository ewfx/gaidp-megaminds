import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def suggest_remediation(observations):
    prompt = f"Suggest remediation actions for the following flagged transactions:\n{observations}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
    )

    return response["choices"][0]["message"]["content"]
