from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

SYSTEM_PROMPT = """
You are AI Law Assist.
Rules:
1. Give only general legal information.
2. Do not give final legal advice.
3. Suggest consulting a lawyer.
"""

def law_agent(user_message):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content
