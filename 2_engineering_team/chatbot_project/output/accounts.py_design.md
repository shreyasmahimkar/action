```markdown
# Accounts Module Design

The `accounts.py` module is designed to provide a stock market chatbot with functionalities to answer various questions related to stocks. Here is the detailed design for the module:

## Class: Account

The `Account` class will serve as the primary interface for interacting with stock market data. It will contain methods to handle all relevant queries about stocks.

### Methods

#### 1. `__init__(self, api_key: str)`

- **Description:** Initializes the `Account` instance with the necessary API key required to communicate with the stock data provider.
- **Parameters:**
  - `api_key` (str): The API key for accessing stock market data.

#### 2. `get_current_price(self, stock_symbol: str) -> float`

- **Description:** Fetches the current price of the specified stock.
- **Parameters:**
  - `stock_symbol` (str): The ticker symbol of the stock to query.
- **Returns:** (float) The current price of the stock.

#### 3. `get_price_history(self, stock_symbol: str, start_date: str, end_date: str) -> dict`

- **Description:** Retrieves the historical prices of a stock between two dates.
- **Parameters:**
  - `stock_symbol` (str): The ticker symbol of the stock.
  - `start_date` (str): The start date for the price history in format `YYYY-MM-DD`.
  - `end_date` (str): The end date for the price history in format `YYYY-MM-DD`.
- **Returns:** (dict) A dictionary containing dates as keys and prices as values.

#### 4. `get_stock_performance(self, stock_symbol: str, start_date: str, end_date: str) -> dict`

- **Description:** Calculates the performance of a stock over a given date range.
- **Parameters:**
  - `stock_symbol` (str): The ticker symbol of the stock.
  - `start_date` (str): The start date for performance evaluation in format `YYYY-MM-DD`.
  - `end_date` (str): The end date for performance evaluation in format `YYYY-MM-DD`.
- **Returns:** (dict) A dictionary with performance metrics such as percentage change, high, low, etc.

#### 5. `get_news(self, stock_symbol: str) -> list`

- **Description:** Retrieves recent news articles related to the specified stock.
- **Parameters:**
  - `stock_symbol` (str): The ticker symbol of the stock.
- **Returns:** (list) A list of news articles where each element contains headline and summary.

#### 6. `get_earnings(self, stock_symbol: str) -> dict`

- **Description:** Fetches the latest earnings report of the specified stock.
- **Parameters:**
  - `stock_symbol` (str): The ticker symbol of the stock.
- **Returns:** (dict) A dictionary containing earnings details such as EPS, revenue, etc.

### Implementation Notes

- The class should leverage a stock market API to fetch real-time data. This will need network connectivity and proper error handling if the API is unreachable or returns errors.
- Additional helper functions may be included to handle data formatting or conversion tasks.
- Security measures should be implemented to ensure that the API key is protected and not exposed.
```

This design thoroughly outlines the methods and their purposes, including parameters and return types, to guide the backend developer in implementing the functionality required for the stock market chatbot application.