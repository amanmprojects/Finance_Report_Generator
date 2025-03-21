import matplotlib.pyplot as plt
import numpy as np
import openai
from langchain.chains import LLMChain
from prompts import MARKET_TRENDS_PROMPT, FINANCIAL_PROJECTIONS_PROMPT, INVESTMENT_RECOMMENDATIONS_PROMPT
import os
from dotenv import load_dotenv
import pandas as pd
import re
import yfinance as yf
from datetime import datetime, timedelta

load_dotenv()

def clean_model_output(text):
    """Remove text within <think> tags from model output."""
    return re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)

def setup_client():
    """Initialize the OpenAI client with Together AI API."""
    return openai.OpenAI(
        api_key=os.getenv("TOGETHER_API_KEY", ""),
        base_url="https://api.together.xyz/v1",
    )

def generate_completion(prompt_text):
    """Generate completion using Together AI via OpenAI SDK."""
    client = setup_client()
    response = client.chat.completions.create(
        model=os.getenv("MODEL_NAME", "deepseek-ai/DeepSeek-R1"),
        messages=[{"role": "user", "content": prompt_text}],
        temperature=0.7,
        max_tokens=2000
    )
    return clean_model_output(response.choices[0].message.content)

def generate_market_trends_report(company, industry, timeframe):
    """Generate market trends report using Together AI."""
    prompt = MARKET_TRENDS_PROMPT.format(company=company, industry=industry, timeframe=timeframe)
    return generate_completion(prompt)

def generate_financial_projections(company, timeframe, metrics):
    """Generate financial projections using Together AI."""
    prompt = FINANCIAL_PROJECTIONS_PROMPT.format(company=company, timeframe=timeframe, metrics=metrics)
    return generate_completion(prompt)

def generate_investment_recommendations(company, risk_profile, investment_horizon):
    """Generate investment recommendations using Together AI."""
    prompt = INVESTMENT_RECOMMENDATIONS_PROMPT.format(company=company, risk_profile=risk_profile, investment_horizon=investment_horizon)
    return generate_completion(prompt)

def create_trend_visualization(data, title, xlabel, ylabel):
    """Create a line plot visualization for trends."""
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data.values, marker='o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    return plt.gcf()

def create_bar_chart(data, title, xlabel, ylabel):
    """Create a bar chart visualization."""
    plt.figure(figsize=(10, 6))
    plt.bar(data.index, data.values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.grid(True)
    return plt.gcf()

def generate_mock_data():
    """Generate mock financial data for visualization."""
    np.random.seed(42)
    dates = pd.date_range(start='2024-01-01', periods=12, freq='M')
    revenue = np.random.normal(1000000, 100000, 12).cumsum()
    profit = np.random.normal(200000, 50000, 12).cumsum()
    
    return {
        'revenue': pd.Series(revenue, index=dates),
        'profit': pd.Series(profit, index=dates)
    }

def get_stock_data(ticker_symbol, period="1y"):
    """
    Fetch real-time stock data for a given ticker symbol.
    
    Args:
        ticker_symbol (str): The stock ticker symbol (e.g., 'AAPL' for Apple)
        period (str): The time period to fetch data for (e.g., '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max')
    
    Returns:
        dict: Dictionary containing stock data and metadata
    """
    try:
        # Create a Ticker object
        ticker = yf.Ticker(ticker_symbol)
        
        # Get historical data
        hist = ticker.history(period=period)
        
        # Get current stock info
        info = ticker.info
        
        # Get recent news
        news = ticker.news
        
        return {
            'historical_data': hist,
            'current_price': info.get('currentPrice', None),
            'market_cap': info.get('marketCap', None),
            'volume': info.get('volume', None),
            'news': news[:5] if news else []  # Get latest 5 news items
        }
    except Exception as e:
        return {'error': str(e)}

def create_stock_visualization(historical_data, title, xlabel="Date", ylabel="Price"):
    """
    Create a stock price visualization with volume.
    
    Args:
        historical_data (pd.DataFrame): Historical stock data from yfinance
        title (str): Chart title
        xlabel (str): X-axis label
        ylabel (str): Y-axis label
    
    Returns:
        matplotlib.figure.Figure: The generated figure
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), height_ratios=[3, 1])
    
    # Plot price
    ax1.plot(historical_data.index, historical_data['Close'], label='Close Price')
    ax1.set_title(title)
    ax1.set_ylabel(ylabel)
    ax1.grid(True)
    ax1.legend()
    
    # Plot volume
    ax2.bar(historical_data.index, historical_data['Volume'], color='gray', alpha=0.5)
    ax2.set_xlabel(xlabel)
    ax2.set_ylabel('Volume')
    ax2.grid(True)
    
    plt.tight_layout()
    return fig 