import matplotlib.pyplot as plt
import numpy as np
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from prompts import MARKET_TRENDS_PROMPT, FINANCIAL_PROJECTIONS_PROMPT, INVESTMENT_RECOMMENDATIONS_PROMPT
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

def setup_llm():
    """Initialize the Groq LLM with the specified model."""
    return ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="deepseek-r1-distill-llama-70b",
        temperature=0.7,
        max_tokens=2000
    )

def generate_market_trends_report(company, industry, timeframe):
    """Generate market trends report using Langchain."""
    llm = setup_llm()
    chain = LLMChain(llm=llm, prompt=MARKET_TRENDS_PROMPT)
    return chain.run(company=company, industry=industry, timeframe=timeframe)

def generate_financial_projections(company, timeframe, metrics):
    """Generate financial projections using Langchain."""
    llm = setup_llm()
    chain = LLMChain(llm=llm, prompt=FINANCIAL_PROJECTIONS_PROMPT)
    return chain.run(company=company, timeframe=timeframe, metrics=metrics)

def generate_investment_recommendations(company, risk_profile, investment_horizon):
    """Generate investment recommendations using Langchain."""
    llm = setup_llm()
    chain = LLMChain(llm=llm, prompt=INVESTMENT_RECOMMENDATIONS_PROMPT)
    return chain.run(company=company, risk_profile=risk_profile, investment_horizon=investment_horizon)

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