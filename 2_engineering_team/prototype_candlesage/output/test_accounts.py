import unittest
from unittest.mock import patch
import pandas as pd
import numpy as np
from accounts import mock_data_loader, predict_with_hmm, predict_with_xgboost, ai_chat

class TestAccounts(unittest.TestCase):
    def test_mock_data_loader(self):
        data = mock_data_loader('AAPL')
        self.assertEqual(len(data), 365)
        self.assertIn('open', data.columns)
        self.assertIn('close', data.columns)

    @patch('accounts.hmm.GaussianHMM')
    def test_predict_with_hmm(self, MockHMM):
        mock_hmm_instance = MockHMM.return_value
        mock_hmm_instance.predict.return_value = np.array([0, 1, 2] * 122 + [0])
        data = mock_data_loader('AAPL')
        result = predict_with_hmm('AAPL', data)
        self.assertIn('next_state', result)

    @patch('accounts.xgb.XGBRegressor')
    def test_predict_with_xgboost(self, MockXGB):
        mock_xgb_instance = MockXGB.return_value
        mock_xgb_instance.predict.return_value = np.random.rand(73)
        data = mock_data_loader('AAPL')
        result = predict_with_xgboost('AAPL', data)
        self.assertIn('predictions', result)
        self.assertEqual(len(result['predictions']), 5)

    @patch('accounts.openai.Completion.create')
    def test_ai_chat(self, mock_openai_create):
        mock_openai_create.return_value.choices = [type('',(object,),{'text':'response text'})()]
        result = ai_chat("Tell me about AAPL stock price trends")
        self.assertEqual(result, 'response text')

if __name__ == '__main__':
    unittest.main()