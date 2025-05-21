import streamlit as st
from accounts import Account, StockAnalysis, News, Forecast, MachineLearningModels, AIChat, mock_data_loader

# Initialize backend classes
account = Account()
stock_analysis = StockAnalysis()
news = News()
forecast = Forecast()
ml_models = MachineLearningModels()
ai_chat = AIChat()
mock_data = mock_data_loader()

# Define streamlit app
def main():
    st.title("Stock and Crypto Analysis")

    # Authentication
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if not st.session_state['logged_in']:
        login_section()
    else:
        dashboard()

def login_section():
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if account.login(username, password):
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            dashboard()
        else:
            st.error("Invalid credentials")

def dashboard():
    st.sidebar.header("Dashboard")
    st.sidebar.button("Logout", on_click=logout)

    page = st.sidebar.radio("Navigation", ["Home", "Analysis", "News", "Forecast", "Backtest", "AI Chat", "Settings", "Help"])

    if page == "Home":
        st.subheader("Welcome to the Dashboard")
    elif page == "Analysis":
        analysis_page()
    elif page == "News":
        news_page()
    elif page == "Forecast":
        forecast_page()
    elif page == "Backtest":
        backtest_page()
    elif page == "AI Chat":
        ai_chat_page()
    elif page == "Settings":
        st.subheader("User Settings")
    elif page == "Help":
        st.subheader("Help and Support")

def logout():
    st.session_state['logged_in'] = False
    st.session_state.pop('username', None)
    st.rerun()

def analysis_page():
    symbol = st.text_input("Enter stock/crypto symbol", "AAPL")
    if st.button("Analyze"):
        st.subheader(f"Statistical Analysis of {symbol}")
        stats = stock_analysis.get_statistical_analysis(symbol)
        st.json(stats)

        st.subheader(f"Technical Analysis of {symbol}")
        tech = stock_analysis.get_technical_analysis(symbol)
        st.json(tech)

def news_page():
    symbol = st.text_input("Enter stock/crypto symbol", "AAPL")
    if st.button("Get News"):
        st.subheader(f"News about {symbol}")
        news_data = news.get_news(symbol)
        st.json(news_data)

def forecast_page():
    symbol = st.text_input("Enter stock/crypto symbol", "AAPL")
    if st.button("Forecast"):
        st.subheader(f"7-day Forecast of {symbol}")
        forecast_data = forecast.forecast_next_7_days(symbol)
        st.line_chart(forecast_data)

def backtest_page():
    st.subheader("Backtest Feature Coming Soon")

def ai_chat_page():
    symbol = st.text_input("Enter stock/crypto symbol", "AAPL")
    question = st.text_input("Ask AI a Question")
    if st.button("Chat with AI"):
        response = ai_chat.chat_with_ai(symbol, question)
        st.text(response)

if __name__ == "__main__":
    main()