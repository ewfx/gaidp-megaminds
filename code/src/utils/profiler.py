import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import openai
import config


# Set OpenAI API Key
openai.api_key = config.OPENAI_API_KEY

def generate_profiling_rules(instructions):
    """Generate data profiling rules using OpenAI LLM."""
    prompt = f"Extract data profiling rules from the following regulatory instructions:\n\n{instructions}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a compliance expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    
    return response["choices"][0]["message"]["content"]  # Extract text response

# Sample regulatory instructions
regulatory_instructions = "Transaction Amount should match Reported Amount, except for cross-currency cases where a 1% deviation is allowed."

# Generate profiling rules
rules = generate_profiling_rules(regulatory_instructions)

# Print the rules
print("\nGenerated Profiling Rules:\n")
print(rules)

# Save rules to a file
output_file = os.path.join(os.path.dirname(__file__), "profiling_rules.txt")
with open(output_file, "w") as file:
    file.write(rules)

print(f"\nProfiling rules saved to {output_file}")
