from openai import OpenAI

client = OpenAI()

# Assistant ID corretto
ASSISTANT_ID = "asst_40N1uMyEll4eIkcq8hJSCvtT"

response = client.chat.completions.create(
    model="gpt-4o",
    tools=[
        {
            "type": "file_search",
            "file_search": {
                "assistant_id": ASSISTANT_ID
            }
        }
    ],
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

