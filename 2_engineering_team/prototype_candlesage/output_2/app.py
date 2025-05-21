import streamlit as st
from accounts import Account

account = Account('testuser', 'testpassword')

def main():
    st.title("Stock/Crypto Currency Analysis")
    
    # Authentication
    authenticated = False
    if st.button("Login"):
        username = st.text_input("Username", value="testuser")
        password = st.text_input("Password", value="testpassword", type="password")
        authenticated = account.login(username, password)
    
    if authenticated:
        st.success("Logged in successfully.")
        st.sidebar.title("Navigation")
        options = ["Home", "Analysis", "News", "Forecast", "Backtest", "AI Chat", "Settings", "Help"]
        choice = st.sidebar.radio("Select Option", options)
        
        if choice == "Home":
            st.subheader("Dashboard")
            st.write("Welcome to the Stock/Crypto Currency Analysis Dashboard.")
        
        elif choice == "Analysis":
            st.subheader("Statistical and Technical Analysis")
            symbol = st.text_input("Enter Stock/Crypto Symbol")
            if st.button("Submit Symbol"):
                stat_analysis = account.get_statistical_analysis(symbol)
                tech_analysis = account.get_technical_analysis(symbol)
                st.write("Statistical Analysis:", stat_analysis)
                st.write("Technical Analysis:", tech_analysis)
                st.write("Hidden Markov Model Prediction:", account.hidden_markov_model_prediction(symbol))
                st.write("XGBoost Model Prediction:", account.xgboost_prediction(symbol))
        
        elif choice == "News":
            st.subheader("Market News")
            symbol = st.text_input("Enter Stock/Crypto Symbol")
            if st.button("Submit Symbol"):
                news = account.get_news(symbol)
                st.write("News About {}: {}".format(symbol.upper(), news))
        
        elif choice == "Forecast":
            st.subheader("Time Series Forecast")
            symbol = st.text_input("Enter Stock/Crypto Symbol")
            if st.button("Submit Symbol"):
                forecast = account.forecast_time_series(symbol)
                st.write("7-Day Forecast for {}: {}".format(symbol.upper(), forecast))
        
        elif choice == "Backtest":
            st.subheader("Backtest Stock/Crypto")
            symbol = st.text_input("Enter Stock/Crypto Symbol")
            days = st.number_input("Enter number of days for backtest", min_value=1, max_value=365, step=1)
            if st.button("Submit"):
                backtest_result = account.backtest(symbol, days)
                st.write("Backtest Result: ", backtest_result)
        
        elif choice == "AI Chat":
            st.subheader("AI Chat")
            question = st.text_area("Enter your query about a Stock/Crypto")
            if st.button("Ask AI"):
                response = account.ai_chat(question)
                st.write("AI Response: ", response)
        
    else:
        st.error("Login failed! Please check your credentials.")
        st.write("Access AI features. Please login to the website.")
        
if __name__ == "__main__":
    main()