import streamlit as st
import pandas as pd
from datetime import datetime
from accounts import predict_with_hmm, predict_with_xgboost, mock_data_loader, ai_chat

# Mockup function to simulate news retrieval
def get_news(symbol):
    return [f"News about {symbol}: Market movements are optimistic.", 
            f"News about {symbol}: Analysts predict a surge in price."]

# Mockup function for time series forecast
def forecast(symbol):
    return [f"{datetime.today().date() + timedelta(days=i)}: Predicted price {100 + i * 2}" for i in range(7)]

# Initialize Session State
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Landing Page: Sign Up / Log In Section
st.title("Stock/Crypto Analysis App")
if not st.session_state['logged_in']:
    sign_option = st.radio("Sign Up / Log In", ('Sign Up', 'Log In'))
    if sign_option == 'Log In':
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Log In") and username == "testuser" and password == "testpassword":
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.session_state['profile_pic'] = "https://via.placeholder.com/150"
    elif sign_option == 'Sign Up':
        new_username = st.text_input("Choose a Username")
        new_password = st.text_input("Choose a Password", type="password")
        if st.button("Sign Up"):
            st.write("Creating your profile...")
            # Mock creation of profile
            st.session_state['logged_in'] = True
            st.session_state['username'] = new_username
            st.session_state['profile_pic'] = "https://via.placeholder.com/150"

    st.markdown("### For more features, please Log In or Sign Up.")
else:
    # Main Dashboard After Log In
    st.sidebar.header("Navigation")
    page = st.sidebar.selectbox("Go to", ["Home", "Analysis", "News", "Forecast", "Backtest", "AI Chat", "Settings", "Help"])
    st.sidebar.text(f"Logged in as: {st.session_state['username']}")
    st.sidebar.image(st.session_state['profile_pic'], width=50)
    if st.sidebar.button("Log Out"):
        st.session_state['logged_in'] = False

    st.header(page)

    # Home Dashboard
    if page == "Home":
        st.write("Welcome to the Dashboard. Choose an option from the sidebar.")

    # Analysis Section
    if page == "Analysis":
        symbol = st.text_input("Enter Stock/Crypto Symbol", "AAPL")
        if st.button("Submit"):
            data = mock_data_loader(symbol)
            st.subheader(f"Statistical Analysis of {symbol}")
            st.dataframe(data.describe())
            st.subheader(f"Technical Analysis of {symbol}")
            hmm_pred = predict_with_hmm(symbol, data)
            xgb_pred = predict_with_xgboost(symbol, data)
            st.write(f"HMM Prediction for next state: {hmm_pred['next_state']}")
            st.write(f"XGBoost latest predictions: {xgb_pred['predictions']}")

    # News Section
    if page == "News":
        symbol = st.text_input("Enter Stock/Crypto Symbol", "AAPL")
        if st.button("Get News"):
            news_articles = get_news(symbol)
            for article in news_articles:
                st.subheader(article)

    # Forecast Section
    if page == "Forecast":
        symbol = st.text_input("Enter Stock/Crypto Symbol", "AAPL")
        if st.button("Forecast"):
            forecasts = forecast(symbol)
            st.subheader(f"7-Day Forecast for {symbol}")
            for day in forecasts:
                st.write(day)
    
    # AI Chat Section
    if page == "AI Chat":
        user_input = st.text_area("Ask the AI about Stocks/Crypto")
        if st.button("Chat"):
            response = ai_chat(user_input)
            st.write(f"AI Response: {response}")

    # Backtest Placeholder
    if page == "Backtest":
        st.write("Backtest feature coming soon.")

    # Settings Placeholder
    if page == "Settings":
        st.write("Settings feature coming soon.")

    # Help & Support Placeholder
    if page == "Help":
        st.write("Help section feature coming soon.")