from openai import OpenAI

client = OpenAI()

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
    messages=[
        {
            "role": "user",
            "content": "Qual è il fatturato di ENI nel 2023?"
        }
    ]
)

print(response.choices[0].message)

