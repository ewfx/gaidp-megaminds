import openai
import json
from config import OPENAI_API_KEY, RULES_PATH

openai.api_key = OPENAI_API_KEY

def generate_profiling_rules(regulation_text):
    prompt = f"Extract key data validation rules from this regulation:\n{regulation_text}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an expert in regulatory reporting."},
                  {"role": "user", "content": prompt}],
    )
    
    rules = response["choices"][0]["message"]["content"]
    
    # Save rules
    with open(f"{RULES_PATH}/profiling_rules.json", "w") as file:
        json.dump(rules, file, indent=4)

    return rules
