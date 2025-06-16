from openai import OpenAI

client = OpenAI()

# 👉 Usa lo stesso Assistant ID
ASSISTANT_ID = "asst_40N1uMyEll4eIkcq8hJSCvtT"

# Fai la domanda in modo moderno usando Responses API
response = client.chat.completions.create(
    model="gpt-4o",
    tools=[{"type": "file_search"}],
    tool_choice="auto",
    messages=[
        {
            "role": "system",
            "content": "Sei un assistente esperto di bilanci. Rispondi solo usando i file caricati."
        },
        {
            "role": "user",
            "content": "Qual è il fatturato di ENI nel 2023?"
        }
    ]
)

print(response.choices[0].message)
