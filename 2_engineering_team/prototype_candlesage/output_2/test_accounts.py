from accounts import Account
import unittest

class TestAccount(unittest.TestCase):
    def setUp(self):
        # Setup a test account
        self.account = Account('testuser', 'testpassword')

    def test_login_success(self):
        self.assertTrue(self.account.login('testuser', 'testpassword'))

    def test_login_failure(self):
        self.assertFalse(self.account.login('testuser', 'wrongpassword'))

    def test_signup(self):
        self.account.signup({'username': 'newuser', 'password': 'newpassword'})
        self.assertTrue(self.account.login('newuser', 'newpassword'))

    def test_get_statistical_analysis(self):
        expected = {'mean': 150, 'variance': 5}
        self.assertEqual(self.account.get_statistical_analysis('AAPL'), expected)

    def test_get_statistical_analysis_invalid(self):
        self.assertEqual(self.account.get_statistical_analysis('INVALID'), {})

    def test_get_technical_analysis(self):
        expected = {'rsi': 70, 'macd': 1.5}
        self.assertEqual(self.account.get_technical_analysis('AAPL'), expected)
        
    def test_get_technical_analysis_invalid(self):
        self.assertEqual(self.account.get_technical_analysis('INVALID'), {})

    def test_get_news(self):
        expected = ['AAPL hits new high!', 'AAPL announces new product.']
        self.assertEqual(self.account.get_news('AAPL'), expected)
        
    def test_get_news_invalid(self):
        self.assertEqual(self.account.get_news('INVALID'), [])

    def test_forecast_time_series(self):
        expected = [100, 101, 102, 103, 104, 105, 106]
        self.assertEqual(self.account.forecast_time_series('AAPL'), expected)
        
    def test_hidden_markov_model_prediction(self):
        self.assertEqual(self.account.hidden_markov_model_prediction('AAPL'), 'Bullish')
        self.assertEqual(self.account.hidden_markov_model_prediction('BTC'), 'Bearish')

    def test_xgboost_prediction(self):
        self.assertEqual(self.account.xgboost_prediction('AAPL'), 'Upward')
        self.assertEqual(self.account.xgboost_prediction('BTC'), 'Downward')

    def test_backtest(self):
        expected = {'symbol': 'AAPL', 'days': 30, 'result': 'Success'}
        self.assertEqual(self.account.backtest('AAPL', 30), expected)

    def test_ai_chat(self):
        question = 'Tell me about AAPL'
        expected = "This is a response from the AI about your query on Tell me about AAPL"
        self.assertEqual(self.account.ai_chat(question), expected)

    def test_access_ai_features_logged_in(self):
        self.assertEqual(self.account.access_ai_features(True), "Access granted to AI features.")

    def test_access_ai_features_not_logged_in(self):
        self.assertEqual(self.account.access_ai_features(False), "Please login to access AI features.")

if __name__ == '__main__':
    unittest.main()