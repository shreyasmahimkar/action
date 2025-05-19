import yfinance as yf
import pandas as pd
from datetime import datetime

class Account:
    def __init__(self, api_key: str):
        """
        Initializes the Account instance with the necessary API key.
        
        Args:
            api_key (str): The API key for accessing stock market data.
        """
        self.api_key = api_key
        # For this implementation, we'll primarily use yfinance which doesn't require an API key
        # But we'll store the API key for potential future use with other services
    
    def get_current_price(self, stock_symbol: str) -> float:
        """
        Fetches the current price of the specified stock.
        
        Args:
            stock_symbol (str): The ticker symbol of the stock to query.
            
        Returns:
            float: The current price of the stock.
        """
        try:
            stock = yf.Ticker(stock_symbol)
            todays_data = stock.history(period='1d')
            if not todays_data.empty:
                return float(todays_data['Close'].iloc[-1])
            else:
                raise ValueError(f"No price data available for {stock_symbol}")
        except Exception as e:
            raise Exception(f"Error fetching current price for {stock_symbol}: {str(e)}")
    
    def get_price_history(self, stock_symbol: str, start_date: str, end_date: str) -> dict:
        """
        Retrieves the historical prices of a stock between two dates.
        
        Args:
            stock_symbol (str): The ticker symbol of the stock.
            start_date (str): The start date for the price history in format YYYY-MM-DD.
            end_date (str): The end date for the price history in format YYYY-MM-DD.
            
        Returns:
            dict: A dictionary containing dates as keys and prices as values.
        """
        try:
            stock = yf.Ticker(stock_symbol)
            hist = stock.history(start=start_date, end=end_date)
            
            price_history = {}
            for date, row in hist.iterrows():
                price_history[date.strftime('%Y-%m-%d')] = float(row['Close'])
            
            return price_history
        except Exception as e:
            raise Exception(f"Error fetching price history for {stock_symbol}: {str(e)}")
    
    def get_stock_performance(self, stock_symbol: str, start_date: str, end_date: str) -> dict:
        """
        Calculates the performance of a stock over a given date range.
        
        Args:
            stock_symbol (str): The ticker symbol of the stock.
            start_date (str): The start date for performance evaluation in format YYYY-MM-DD.
            end_date (str): The end date for performance evaluation in format YYYY-MM-DD.
            
        Returns:
            dict: A dictionary with performance metrics such as percentage change, high, low, etc.
        """
        try:
            stock = yf.Ticker(stock_symbol)
            hist = stock.history(start=start_date, end=end_date)
            
            if hist.empty:
                raise ValueError(f"No data available for {stock_symbol} in the specified date range")
            
            start_price = hist['Close'].iloc[0]
            end_price = hist['Close'].iloc[-1]
            price_change = end_price - start_price
            percent_change = (price_change / start_price) * 100
            
            performance = {
                'start_price': float(start_price),
                'end_price': float(end_price),
                'price_change': float(price_change),
                'percent_change': float(percent_change),
                'highest_price': float(hist['High'].max()),
                'lowest_price': float(hist['Low'].min()),
                'avg_volume': float(hist['Volume'].mean())
            }
            
            return performance
        except Exception as e:
            raise Exception(f"Error calculating performance for {stock_symbol}: {str(e)}")

    def get_news(self, stock_symbol: str) -> list:
        """
        Retrieves recent news articles related to the specified stock.
        
        Args:
            stock_symbol (str): The ticker symbol of the stock.
            
        Returns:
            list: A list of news articles where each element contains headline and summary.
        """
        try:
            stock = yf.Ticker(stock_symbol)
            news = stock.news
            
            # If no news available, return empty list with message
            if not news:
                return [{
                    'headline': 'No recent news available',
                    'summary': f'No recent news articles found for {stock_symbol}',
                    'link': '',
                    'publisher': '',
                    'published': ''
                }]
            
            formatted_news = []
            for article in news:
                news_item = {
                    'headline': article.get('title', 'No title available'),
                    'summary': article.get('summary', 'No summary available'),
                    'link': article.get('link', 'No link available'),
                    'publisher': article.get('publisher', 'Unknown publisher'),
                    'published': article.get('providerPublishTime', 'Unknown date')
                }
                formatted_news.append(news_item)
            
            return formatted_news
        except Exception as e:
            raise Exception(f"Error fetching news for {stock_symbol}: {str(e)}")
    
    def get_earnings(self, stock_symbol: str) -> dict:
        """
        Fetches the latest earnings report of the specified stock.
        
        Args:
            stock_symbol (str): The ticker symbol of the stock.
            
        Returns:
            dict: A dictionary containing earnings details such as EPS, revenue, etc.
        """
        try:
            stock = yf.Ticker(stock_symbol)
            
            # Get the income statement for earnings data
            income_stmt = stock.income_stmt
            
            # Get the quarterly financials if available
            quarterly_financials = stock.quarterly_financials
            
            result = {
                'latest_year': None,
                'latest_quarter': None,
                'latest_eps': None,
                'latest_report': {}
            }
            
            # Extract latest year and quarter earnings
            if income_stmt is not None and not income_stmt.empty:
                # Get the most recent date (column)
                latest_date = income_stmt.columns[0]
                result['latest_year'] = latest_date.year if hasattr(latest_date, 'year') else str(latest_date)
                
                # Get Net Income
                if 'Net Income' in income_stmt.index:
                    net_income = income_stmt.loc['Net Income', latest_date]
                    result['latest_eps'] = float(net_income) if not pd.isna(net_income) else None
            
            # Get quarterly info if available
            if quarterly_financials is not None and not quarterly_financials.empty:
                latest_quarter = quarterly_financials.columns[0]
                result['latest_quarter'] = latest_quarter.strftime('%Y-Q%q') if hasattr(latest_quarter, 'strftime') else str(latest_quarter)
            
            # Try to get some basic earnings info
            try:
                info = stock.info
                if 'trailingEps' in info:
                    result['trailing_eps'] = info['trailingEps']
                if 'forwardEps' in info:
                    result['forward_eps'] = info['forwardEps']
                if 'pegRatio' in info:
                    result['peg_ratio'] = info['pegRatio']
            except:
                pass  # If info retrieval fails, continue without it
            
            return result
        except Exception as e:
            raise Exception(f"Error fetching earnings for {stock_symbol}: {str(e)}")