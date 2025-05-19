import streamlit as st
from agents import Agent
from dotenv import load_dotenv
import os

# Load API key
load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize Agent (replace with correct SDK usage if needed)
agent = Agent(
    name="Jokester",
    instructions="You are a joke teller",
    model="gpt-4.1-mini",
)

st.set_page_config(page_title="Jokester Chatbot", layout="centered")
st.title("Jokester 🤡 - Your AI Joke Teller")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input box for user
if prompt := st.chat_input("Tell me a joke or ask anything!"):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate agent response
    with st.chat_message("assistant"):
        with st.spinner("Jokester is thinking..."):
            # Combine all messages for context
            history = [
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ]
            # Get response from agent using the agent instance
            response = agent.run(prompt, history=history)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
