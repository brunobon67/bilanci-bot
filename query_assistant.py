from openai import OpenAI

client = OpenAI()

# ✅ Il tuo Assistant ID
ASSISTANT_ID = "asst_40N1uMyEll4eIkcq8hJSCvtT"

response = client.chat.completions.create(
    model="gpt-4o",
    tools=[
        {
            "type": "function",
            "function": {
                "name": "file_search",
                "parameters": {
                    "assistant_id": ASSISTANT_ID
                }
            }
        }
    ],
    tool_choice="auto",
    messages=[
        {
            "role": "system",
            "content": "Sei un assistente finanziario esperto di bilanci. Rispondi solo usando i file del bilancio caricati. Se non trovi l'informazione, di' che non la sai."
        },
        {
            "role": "user",
            "content": "Qual è il fatturato di ENI nel 2023?"
        }
    ]
)

print(response.choices[0].message)
