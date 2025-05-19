import gradio as gr
from accounts import Account
from datetime import datetime, timedelta
import json

# Initialize the account with a mock API key
api_key = "mock_api_key"
account = Account(api_key)

def format_news(news_list):
    formatted = ""
    for i, news in enumerate(news_list, 1):
        formatted += f"{i}. {news['headline']}\n"
        formatted += f"   Summary: {news['summary']}\n"
        formatted += f"   Publisher: {news['publisher']}\n"
        formatted += f"   Link: {news['link']}\n\n"
    return formatted

def format_performance(performance_data):
    result = "Performance Summary:\n"
    result += f"Start Price: ${performance_data['start_price']:.2f}\n"
    result += f"End Price: ${performance_data['end_price']:.2f}\n"
    result += f"Price Change: ${performance_data['price_change']:.2f}\n"
    result += f"Percent Change: {performance_data['percent_change']:.2f}%\n"
    result += f"Highest Price: ${performance_data['highest_price']:.2f}\n"
    result += f"Lowest Price: ${performance_data['lowest_price']:.2f}\n"
    result += f"Average Volume: {int(performance_data['avg_volume'])}"
    return result

def format_earnings(earnings_data):
    result = "Earnings Information:\n"
    for key, value in earnings_data.items():
        if key == 'latest_report':
            continue  # Skip the detailed report for simplicity
        if value is not None:
            result += f"{key.replace('_', ' ').title()}: {value}\n"
    return result

def format_price_history(price_history):
    result = "Price History:\n"
    for date, price in price_history.items():
        result += f"{date}: ${price:.2f}\n"
    return result

def chatbot(message, history):
    try:
        message = message.lower().strip()
        
        # Check for current price queries
        if "current price" in message or "price now" in message:
            # Extract stock symbol
            for word in message.split():
                word = word.strip(",.!?:;'\"")
                if word.isalpha() and len(word) >= 1 and len(word) <= 5 and word not in ["what", "is", "the", "of", "a", "for", "price", "current"]:
                    try:
                        price = account.get_current_price(word.upper())
                        return f"The current price of {word.upper()} is ${price:.2f}"
                    except Exception as e:
                        continue
            return "I couldn't identify a valid stock symbol in your message. Please specify a stock symbol clearly."
        
        # Check for price history queries
        elif "price history" in message or "historical prices" in message:
            for word in message.split():
                word = word.strip(",.!?:;'\"")
                if word.isalpha() and len(word) >= 1 and len(word) <= 5 and word not in ["what", "is", "the", "of", "a", "for", "price", "history", "historical", "prices"]:
                    try:
                        # Default to last 30 days
                        end_date = datetime.now().strftime("%Y-%m-%d")
                        start_date = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
                        price_history = account.get_price_history(word.upper(), start_date, end_date)
                        return format_price_history(price_history)
                    except Exception as e:
                        continue
            return "I couldn't identify a valid stock symbol in your message. Please specify a stock symbol clearly."
        
        # Check for performance queries
        elif "performance" in message:
            for word in message.split():
                word = word.strip(",.!?:;'\"")
                if word.isalpha() and len(word) >= 1 and len(word) <= 5 and word not in ["what", "is", "the", "of", "a", "for", "performance"]:
                    try:
                        # Default to last 30 days
                        end_date = datetime.now().strftime("%Y-%m-%d")
                        start_date = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
                        performance = account.get_stock_performance(word.upper(), start_date, end_date)
                        return format_performance(performance)
                    except Exception as e:
                        continue
            return "I couldn't identify a valid stock symbol in your message. Please specify a stock symbol clearly."
        
        # Check for news queries
        elif "news" in message:
            for word in message.split():
                word = word.strip(",.!?:;'\"")
                if word.isalpha() and len(word) >= 1 and len(word) <= 5 and word not in ["what", "is", "the", "of", "a", "for", "news", "about"]:
                    try:
                        news = account.get_news(word.upper())
                        return format_news(news)
                    except Exception as e:
                        continue
            return "I couldn't identify a valid stock symbol in your message. Please specify a stock symbol clearly."
        
        # Check for earnings queries
        elif "earnings" in message:
            for word in message.split():
                word = word.strip(",.!?:;'\"")
                if word.isalpha() and len(word) >= 1 and len(word) <= 5 and word not in ["what", "is", "the", "of", "a", "for", "earnings"]:
                    try:
                        earnings = account.get_earnings(word.upper())
                        return format_earnings(earnings)
                    except Exception as e:
                        continue
            return "I couldn't identify a valid stock symbol in your message. Please specify a stock symbol clearly."
        
        # Help message
        else:
            return """I can help you with the following stock market information:
1. Current price: 'What is the current price of AAPL?'
2. Price history: 'Show me the price history of TSLA'
3. Performance: 'How is the performance of MSFT?'
4. News: 'What are the latest news about AMZN?'
5. Earnings: 'Tell me about the earnings of GOOG'

Just ask any of these questions with a valid stock symbol!"""
            
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"

demo = gr.ChatInterface(
    chatbot,
    chatbot=gr.Chatbot(height=500),
    textbox=gr.Textbox(placeholder="Ask about stock market information (e.g., 'What is the current price of AAPL?')"),
    title="Stock Market Chatbot",
    description="Ask questions about stocks such as current prices, price history, performance, news, and earnings.",
    theme="soft",
    examples=[
        "What is the current price of AAPL?",
        "Show me the price history of TSLA",
        "How is the performance of MSFT?",
        "What are the latest news about AMZN?",
        "Tell me about the earnings of GOOG"
    ],
)

if __name__ == "__main__":
    demo.launch()