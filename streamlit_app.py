import streamlit as st
from openai import OpenAI
import time

# Init OpenAI client
client = OpenAI()

ASSISTANT_ID = "asst_40N1uMyEll4eIkcq8hJSCvtT"

st.set_page_config(page_title="BilanciBot 🧾🤖", page_icon="📊")

st.title("📊 BilanciBot - Assistant su PDF")

# Session state per il thread ID e messaggi
if "thread_id" not in st.session_state:
    thread = client.beta.threads.create()
    st.session_state.thread_id = thread.id
    st.session_state.messages = []

# Mostra messaggi precedenti
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Input utente
if user_input := st.chat_input("Fai una domanda sui bilanci..."):
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Aggiungi messaggio all'Assistant
    client.beta.threads.messages.create(
        thread_id=st.session_state.thread_id,
        role="user",
        content=user_input
    )

    # Avvia run
    run = client.beta.threads.runs.create(
        thread_id=st.session_state.thread_id,
        assistant_id=ASSISTANT_ID
    )

    # Polling finché non completa
    while True:
        run_status = client.beta.threads.runs.retrieve(
            thread_id=st.session_state.thread_id,
            run_id=run.id
        )
        if run_status.status == "completed":
            break
        time.sleep(1)

    # Leggi risposta
    messages = client.beta.threads.messages.list(thread_id=st.session_state.thread_id)
    answer = messages.data[0].content[0].text.value

    st.chat_message("assistant").write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
