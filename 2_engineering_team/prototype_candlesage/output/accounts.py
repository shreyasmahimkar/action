import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from hmmlearn import hmm
import xgboost as xgb
import streamlit as st
from agents import Agent
from dotenv import load_dotenv
import os

# Mock Data Loader
def mock_data_loader(symbol: str):
    dates = pd.date_range(end=datetime.today(), periods=365).to_pydatetime().tolist()
    data = {
        'date': dates,
        'open': np.random.rand(365) * 100,
        'high': np.random.rand(365) * 100,
        'low': np.random.rand(365) * 100,
        'close': np.random.rand(365) * 100,
        'volume': np.random.randint(1, 1000, 365)
    }
    df = pd.DataFrame(data)
    df = df.sort_values(by='date')
    return df

# Load Mock Data
mock_aapl_data = mock_data_loader('AAPL')
mock_btc_data = mock_data_loader('BTC')

# Machine Learning Models
def predict_with_hmm(symbol: str, data: pd.DataFrame) -> dict:
    model = hmm.GaussianHMM(n_components=3, covariance_type="diag", n_iter=1000)
    data_values = data[['open', 'high', 'low', 'close']].values
    model.fit(data_values)
    hidden_states = model.predict(data_values)
    next_state = np.random.choice(hidden_states)
    return {'symbol': symbol, 'next_state': next_state}

def predict_with_xgboost(symbol: str, data: pd.DataFrame) -> dict:
    X = data[['open', 'high', 'low', 'volume']]
    y = data['close']
    train_size = int(len(data) * 0.8)
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]
    model = xgb.XGBRegressor(objective ='reg:squarederror')
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    return {'symbol': symbol, 'predictions': predictions[-5:].tolist()}

# Predictions
hmm_result_aapl = predict_with_hmm('AAPL', mock_aapl_data)
xgb_result_aapl = predict_with_xgboost('AAPL', mock_aapl_data)
hmm_result_btc = predict_with_hmm('BTC', mock_btc_data)
xgb_result_btc = predict_with_xgboost('BTC', mock_btc_data)

# --- Streamlit Chatbot Section (Integrated as per your example) ---

def ai_chat(user_input: str):

# Load API key from .env
    load_dotenv(override=True)
    openai_api_key = os.getenv("OPENAI_API_KEY")

    # Initialize Agent
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

    # --- END Streamlit Chatbot Section ---

# If you want to display predictions and data in Streamlit as well, you can add:
st.header("Sample Data & Predictions")
st.subheader("AAPL Mock Data")
st.write(mock_aapl_data.head())
st.subheader("BTC Mock Data")
st.write(mock_btc_data.head())
st.subheader("AAPL HMM Result")
st.write(hmm_result_aapl)
st.subheader("AAPL XGBoost Result")
st.write(xgb_result_aapl)
st.subheader("BTC HMM Result")
st.write(hmm_result_btc)
st.subheader("BTC XGBoost Result")
st.write(xgb_result_btc)
