import gradio as gr
from accounts import Account, StockCryptoAnalysis, MachineLearningModels, UserInterface, Backtest, AIChat

# Instantiate the backend classes
account = Account("testuser", "testpassword", "default.png")
stock_crypto_analysis = StockCryptoAnalysis()
ml_models = MachineLearningModels()
ui = UserInterface()
backtest = Backtest()
ai_chat = AIChat()

# Define functions for gradio interface
def analyze_stock_crypto(symbol):
    data = stock_crypto_analysis.fetch_data(symbol)
    stats = stock_crypto_analysis.statistical_analysis(data)
    technicals = stock_crypto_analysis.technical_analysis(data)
    forecast = stock_crypto_analysis.time_series_forecast(data)
    news = stock_crypto_analysis.news_fetch(symbol)
    return stats, technicals, news, forecast

def user_login(username, password):
    if account.login(username, password):
        profile = account.get_user_profile()
        ui.render_dashboard(profile)
        return "Login Successful"
    else:
        return "Invalid Credentials"

def signup(username, password):
    user_data = account.signup(username, password)
    return f"User {user_data['username']} signed up with profile picture: {user_data['profile_picture']}"

def provide_ai_features_signup():
    ui.prompt_ai_features_signup()
    return "Prompt for AI features signup/login displayed"

def run_backtest(days):
    data = stock_crypto_analysis.fetch_data("AAPL")
    backtest_result = backtest.run_backtest(data, days)
    return backtest_result

def ai_chat_response(message):
    response = ai_chat.chat_with_ai(message)
    return response

# Gradio Interface
def gradio_ui():
    with gr.Blocks() as demo:
        gr.Markdown("# Stock/Crypto Analysis Web App")
        
        with gr.Tab("Landing Page"):
            with gr.Row():
                symbol_input = gr.Textbox(label="Enter Stock/Crypto Symbol")
                submit_button = gr.Button("Submit")

            with gr.Tab("Statistics & News"):
                stats_display = gr.JSON(label="Statistical Analysis")
                technical_display = gr.JSON(label="Technical Analysis")
                news_display = gr.JSON(label="News")
                forecast_display = gr.JSON(label="7-Day Forecast")

            submit_button.click(analyze_stock_crypto, inputs=symbol_input,
                                outputs=[stats_display, technical_display, news_display, forecast_display])
        
        with gr.Tab("Login"):
            username_input = gr.Textbox(label="Username")
            password_input = gr.Textbox(label="Password", type="password")
            login_button = gr.Button("Login")
            login_output = gr.Textbox(label="Login Output")
            login_button.click(user_login, inputs=[username_input, password_input], outputs=login_output)

        with gr.Tab("Signup"):
            signup_username_input = gr.Textbox(label="New Username")
            signup_password_input = gr.Textbox(label="New Password", type="password")
            signup_button = gr.Button("Sign Up")
            signup_output = gr.Text(label="Signup Output")
            signup_button.click(signup, inputs=[signup_username_input, signup_password_input], outputs=signup_output)
        
        with gr.Tab("AI Features"):
            ai_display = gr.Textbox(label="AI Feature Prompt")
            ai_button = gr.Button("Access AI Features")
            ai_button.click(provide_ai_features_signup, inputs=[], outputs=ai_display)

    return demo

if __name__ == "__main__":
    ui_app = gradio_ui()
    ui_app.launch()