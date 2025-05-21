import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from accounts import mock_data_loader, forecast, ai_chat

class TestAccounts(unittest.TestCase):

    def test_mock_data_loader(self):
        data = mock_data_loader()
        self.assertIn('AAPL', data)
        self.assertIn('BTC', data)
        self.assertIsInstance(data['AAPL'], pd.DataFrame)
        self.assertIsInstance(data['BTC'], pd.DataFrame)

    @patch('accounts.Prophet')
    def test_forecast(self, MockProphet):
        mock_data = pd.DataFrame({
            'date': pd.date_range(start='1/1/2020', periods=365),
            'close': [float(i) for i in range(365)]
        })
        mock_model = MagicMock()
        MockProphet.return_value = mock_model
        mock_model.make_future_dataframe.return_value = mock_data
        mock_model.predict.return_value = mock_data
        forecast_data = forecast('AAPL', mock_data)
        self.assertEqual(len(forecast_data), 7)

    @patch('accounts.openai.Completion.create')
    def test_ai_chat(self, mock_openai):
        mock_response = {'choices': [{'text': ' This is a test response.'}]}
        mock_openai.return_value = mock_response
        response = ai_chat('Test prompt')
        self.assertEqual(response, 'This is a test response.')

if __name__ == '__main__':
    unittest.main()