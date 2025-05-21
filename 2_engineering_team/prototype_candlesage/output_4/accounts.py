import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from fbprophet import Prophet
import openai
import random

# Mock data loader for AAPL and Bitcoin
def mock_data_loader():
    date_rng = pd.date_range(end=pd.Timestamp.today(), periods=365, freq='D')
    data_aapl = pd.DataFrame(date_rng, columns=['date'])
    data_aapl['open'] = [random.uniform(100, 150) for _ in range(365)]
    data_aapl['high'] = data_aapl['open'] + random.uniform(0, 10)
    data_aapl['low'] = data_aapl['open'] - random.uniform(0, 10)
    data_aapl['close'] = data_aapl['open'] + random.uniform(-5, 5)
    data_aapl['volume'] = random.randint(1000000, 5000000)
    
    data_btc = pd.DataFrame(date_rng, columns=['date'])
    data_btc['open'] = [random.uniform(30000, 60000) for _ in range(365)]
    data_btc['high'] = data_btc['open'] + random.uniform(0, 1000)
    data_btc['low'] = data_btc['open'] - random.uniform(0, 1000)
    data_btc['close'] = data_btc['open'] + random.uniform(-500, 500)
    data_btc['volume'] = random.randint(1000, 10000)
    
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
st.sidebar.button("Login/Signup")
st.sidebar.button("About")
st.sidebar.button("Contact")

st.sidebar.info("Login to access AI features and Machine Learning models.")