#!/usr/bin/env python
import warnings
import os
from datetime import datetime

from engineering_team.crew import EngineeringTeam

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

requirements = """
A simple Chatbot Application for answering questions about the stock market.
The chatbot should be able to answer questions about the stock market, including:
- What is the current price of a stock?
- What is the price history of a stock?
- What is the performance of a stock?
- What is the news about a stock?
- What is the earnings of a stock?
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