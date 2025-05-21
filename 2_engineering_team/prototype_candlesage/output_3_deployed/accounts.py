class Account:
    def __init__(self, username: str = '', password: str = ''):
        self.username = username
        self.password = password

    def signup(self, username: str, password: str) -> dict:
        # Mock signup functionality
        return {'username': username, 'profile': 'User profile data'}

    def login(self, username: str, password: str) -> bool:
        # Mock login check
        return username == 'testuser' and password == 'testpassword'

    def get_user_profile(self, username: str) -> dict:
        # Returns mock user profile
        return {'username': username, 'profile': 'User profile data'}

class StockAnalysis:
    def get_statistical_analysis(self, symbol: str) -> dict:
        # Returns mock statistical analysis
        return {'symbol': symbol, 'mean_price': 150, 'volatility': 0.3}

    def get_technical_analysis(self, symbol: str) -> dict:
        # Returns mock technical analysis
        return {'symbol': symbol, 'rsi': 55, 'moving_averages': {'MA50': 149, 'MA200': 145}}

class News:
    def get_news(self, symbol: str) -> list:
        # Returns mock news list
        return [{'title': 'Recent News', 'content': 'Market news content here.'}]

class Forecast:
    def forecast_next_7_days(self, symbol: str) -> list:
        # Returns mock forecasted prices
        return [151, 152, 150, 153, 154, 155, 156]

class MachineLearningModels:
    def predict_with_hmm(self, symbol: str) -> str:
        # Mock HMM prediction
        return 'The trend is upward.'

    def predict_with_xgboost(self, symbol: str) -> str:
        # Mock XGBoost prediction
        return 'The trend is downward.'

class AIChat:
    def chat_with_ai(self, symbol: str, question: str) -> str:
        # Mock AI chat response
        return 'AI response regarding the stock or cryptocurrency.'

# Helper function to load mock data
def mock_data_loader() -> dict:
    return {
        'AAPL': {
            'statistics': {'mean_price': 150, 'volatility': 0.3},
            'technical': {'rsi': 55, 'moving_averages': {'MA50': 149, 'MA200': 145}},
            'news': [{'title': 'AAPL News', 'content': 'Latest news on AAPL.'}],
            'forecast': [151, 152, 150, 153, 154, 155, 156],
            'hmm': 'The trend is upward.',
            'xgboost': 'The trend is downward.'
        },
        'BTC': {
            'statistics': {'mean_price': 45000, 'volatility': 0.5},
            'technical': {'rsi': 60, 'moving_averages': {'MA50': 44500, 'MA200': 43000}},
            'news': [{'title': 'BTC News', 'content': 'Latest news on Bitcoin.'}],
            'forecast': [46000, 45500, 45000, 46500, 47000, 47500, 48000],
            'hmm': 'The trend is volatile.',
            'xgboost': 'The trend is bullish.'
        }
    }