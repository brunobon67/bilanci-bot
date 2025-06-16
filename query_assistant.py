from openai import OpenAI
import time

# 👉 Sostituisci con l'ID del tuo Assistant
ASSISTANT_ID = "QUI_METTI_IL_TUO_ASSISTANT_ID"

client = OpenAI()

# Crea un thread di conversazione
thread = client.beta.threads.create()

# Domanda di prova
query = "Qual è il fatturato di ENI nel 2023?"

# Aggiungi messaggio utente
client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=query,
)

# Avvia la run
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=ASSISTANT_ID
)

# Aspetta completamento
while True:
    run_status = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )
    if run_status.status == "completed":
        break
    time.sleep(1)

# Stampa la risposta
messages = client.beta.threads.messages.list(thread_id=thread.id)
for message in messages.data:
    print(f"{message.role}: {message.content[0].text.value}")
