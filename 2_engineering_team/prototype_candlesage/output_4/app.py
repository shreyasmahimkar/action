import streamlit as st
import pandas as pd
from datetime import datetime
from prophet import Prophet
import openai
import random

# Mock data loader for AAPL and Bitcoin
def mock_data_loader():
    date_rng = pd.date_range(end=pd.Timestamp.today(), periods=365, freq='D')
    data_aapl = pd.DataFrame(date_rng, columns=['date'])
    data_aapl['open'] = [random.uniform(100, 150) for _ in range(365)]
    data_aapl['high'] = data_aapl['open'] + [random.uniform(0, 10) for _ in range(365)]
    data_aapl['low'] = data_aapl['open'] - [random.uniform(0, 10) for _ in range(365)]
    data_aapl['close'] = data_aapl['open'] + [random.uniform(-5, 5) for _ in range(365)]
    data_aapl['volume'] = [random.randint(1000000, 5000000) for _ in range(365)]
    
    data_btc = pd.DataFrame(date_rng, columns=['date'])
    data_btc['open'] = [random.uniform(30000, 60000) for _ in range(365)]
    data_btc['high'] = data_btc['open'] + [random.uniform(0, 1000) for _ in range(365)]
    data_btc['low'] = data_btc['open'] - [random.uniform(0, 1000) for _ in range(365)]
    data_btc['close'] = data_btc['open'] + [random.uniform(-500, 500) for _ in range(365)]
    data_btc['volume'] = [random.randint(1000, 10000) for _ in range(365)]
    
    return {'AAPL': data_aapl, 'BTC': data_btc}

# Forecasting using Facebook Prophet model
def forecast(symbol, data):
    model = Prophet(daily_seasonality=True)
    data = data.rename(columns={'date': 'ds', 'close': 'y'})
    model.fit(data)
    future = model.make_future_dataframe(periods=7)
    forecast = model.predict(future)
    return forecast.tail(7)

# AI Chat using OpenAI's GPT-3
def ai_chat(prompt):
    openai.api_key = "your_api_key_here"
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      max_tokens=150
    )
    return response['choices'][0]['text'].strip()

# Streamlit UI
def main():
    st.title("Stock and Cryptocurrency Analysis")
    symbol = st.text_input("Enter the stock/crypto symbol:")
    submit = st.button("Submit")

    if submit:
        data = mock_data_loader()
        if symbol in data:
            st.subheader("Statistical Analysis")
            st.write("Coming soon...")

            st.subheader("Technical Analysis")
            st.write("Coming soon...")

            st.subheader("News")
            st.write("Fetching news...")

            st.subheader("7-Day Forecast")
            forecast_data = forecast(symbol, data[symbol])
            st.write(forecast_data)

    st.sidebar.write("Welcome to our application")
    login_signup_section = st.sidebar.expander("Login/Signup")
    with login_signup_section:
        st.write("Access AI features and Machine Learning models")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username == "testuser" and password == "testpassword":
                st.success(f"Welcome {username}")
                dashboard()
            else:
                st.error("Invalid credentials")

    st.sidebar.button("About")
    st.sidebar.button("Contact")

def dashboard():
    st.sidebar.write("Dashboard")
    st.subheader("Dashboard Features")
    st.write("1. Home (Dashboard)")
    st.write("2. Analysis")
    st.write("3. News")
    st.write("4. Forecast")
    st.write("5. Backtest")
    st.write("6. AI chat")
    st.write("7. Settings")
    st.write("8. Help")

if __name__ == "__main__":
    main()