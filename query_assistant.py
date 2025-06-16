from openai import OpenAI

client = OpenAI()

ASSISTANT_ID = "asst_40N1uMyEll4eIkcq8hJSCvtT"

# ✅ Usa Responses API, NON chat.completions!
response = client.beta.responses.create(
    assistant_id=ASSISTANT_ID,
    model="gpt-4o",
    instructions="Sei un assistente esperto di bilanci. Rispondi solo usando i file caricati.",
    input="Qual è il fatturato di ENI nel 2023?"
)

print(response)
