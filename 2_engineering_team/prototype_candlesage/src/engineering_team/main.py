#!/usr/bin/env python
import warnings
import os
from datetime import datetime

from engineering_team.crew import EngineeringTeam

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

requirements = """
You are going to design and implement a streamlit web application for giving users a statistical and technical analysis of a stock.
Mockup data for AAPL and Bitcoin for past 365 days, if you dont have the data, 
in the following format: date, open, high, low, close, volume 
use the mockup data or mockup data yourself, Mock up the data for statistics, Machine learning , wherever you cannot find the data.
Design a Landing page with the following features look at https://candlesage.streamlit.app/ for the design:
1. Input Box to enter a stock/crypto currency symbol
2. A button to submit the symbol
3. A section to display the statistical analysis of the stock/crypto currency
4. A section to display the technical analysis of the stock/crypto currency
5. A section to display the news about the stock/crypto currency
6. Time Series Forecast of the stock/crypto currency for next 7 days
7. Have 4 Buttons on top right of the page:
8. In the End have some way to tell the user to access AI features and other Machine Learning features login or signup to the website.
if you have access to acadia-analytics.app website, scrape the data from the website and use it as mockup data.
    - Login/Signup
    - About
    - Contact
8. On Signup Use mockup data to create a user profile. Keep storing to the database optional for now.
9. On login use the following credentials:
    - Username: testuser
    - Password: testpassword
10. After login, show a dashboard with the following features:
    - on the right top corner, show a logout button with username and profile picture
    - Rest of the page will have a sidebar with the following features which will be hidden when the user is not logged in:
    - After login, the sidebar will be visible and the following features will be shown and the links will be active:
        - Home (Dashboard)
        - Analysis (Statistical and Technical Analysis)
            - Have Hidden Markov Model for predicting the next state of the stock/crypto currency, use hmmlearn for this task, code it. 
            - Have XGBoost model for predicting the next state of the stock/crypto currency use skikit-learn for this task, code it.
        - News (News about the stock/crypto currency)
        - Forecast (Time Series Forecast of the stock/crypto currency for next 7 days) - should have a nice chart to show the forecasted data with the actual data.
        - Backtest (Backtest the stock/crypto currency for the last X days)
        - AI chat (Chat with the stock/crypto currency)
        - Settings (User Settings)
        - Help (Help and Support)


"""


module_name = "accounts.py"
class_name = "Account"


def run():
    """
    Run the research crew.
    """
    inputs = {
        'requirements': requirements,
        'module_name': module_name,
        'class_name': class_name
    }

    # Create and run the crew
    result = EngineeringTeam().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()