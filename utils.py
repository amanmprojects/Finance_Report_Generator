import matplotlib.pyplot as plt
import numpy as np
import openai
from langchain.chains import LLMChain
from prompts import (
    SYSTEM_CONTEXT,
    MARKET_TRENDS_PROMPT,
    FINANCIAL_PROJECTIONS_PROMPT,
    INVESTMENT_RECOMMENDATIONS_PROMPT,
    EVALUATION_TEMPLATE
)
import os
from dotenv import load_dotenv
import pandas as pd
import re
import yfinance as yf
from datetime import datetime, timedelta
import json
from typing import Dict, List, Union, Optional

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

def generate_completion(prompt_text: str) -> str:
    """Generate completion using Together AI via OpenAI SDK."""
    client = setup_client()
    
    messages = [
        {"role": "system", "content": SYSTEM_CONTEXT},
        {"role": "user", "content": prompt_text}
    ]
    
    try:
        response = client.chat.completions.create(
            model=os.getenv("MODEL_NAME", "deepseek-ai/DeepSeek-R1"),
            messages=messages,
            temperature=0.7,
            max_tokens=2000
        )
        return clean_model_output(response.choices[0].message.content)
    except Exception as e:
        print(f"Error generating completion: {str(e)}")
        return ""

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
    dates = pd.date_range(start='2024-01-01', periods=12, freq='ME')
    revenue = pd.Series(np.random.normal(1000000, 100000, 12).cumsum(), index=dates, name='Close')
    profit = pd.Series(np.random.normal(200000, 50000, 12).cumsum(), index=dates, name='Close')
    
    # Add Volume column for visualization
    volume_revenue = pd.Series(np.random.randint(100000, 1000000, 12), index=dates, name='Volume')
    volume_profit = pd.Series(np.random.randint(50000, 500000, 12), index=dates, name='Volume')
    
    return {
        'revenue': pd.DataFrame({'Close': revenue, 'Volume': volume_revenue}),
        'profit': pd.DataFrame({'Close': profit, 'Volume': volume_profit})
    }

def get_stock_data(ticker_symbol: str, period: str = "1y") -> Dict:
    """Fetch real-time stock data with enhanced error handling."""
    try:
        ticker = yf.Ticker(ticker_symbol)
        hist = ticker.history(period=period)
        info = ticker.info
        news = ticker.news
        
        # Calculate additional metrics
        metrics = calculate_stock_metrics(hist)
        
        return {
            'historical_data': hist,
            'current_price': info.get('currentPrice', None),
            'market_cap': info.get('marketCap', None),
            'volume': info.get('volume', None),
            'metrics': metrics,
            'news': news[:5] if news else [],
            'success': True
        }
    except Exception as e:
        return {
            'error': str(e),
            'success': False
        }

def calculate_stock_metrics(historical_data: pd.DataFrame) -> Dict:
    """Calculate additional stock metrics."""
    metrics = {
        'volatility': 0.0,
        'sma_50': 0.0,
        'sma_200': 0.0,
        'rsi': 50.0  # Default neutral RSI
    }
    
    try:
        if not historical_data.empty and 'Close' in historical_data.columns:
            # Volatility
            metrics['volatility'] = historical_data['Close'].pct_change().std() * np.sqrt(252)
            
            # Moving averages
            if len(historical_data) >= 50:
                metrics['sma_50'] = historical_data['Close'].rolling(window=50).mean().iloc[-1]
            if len(historical_data) >= 200:
                metrics['sma_200'] = historical_data['Close'].rolling(window=200).mean().iloc[-1]
            
            # RSI
            delta = historical_data['Close'].diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
            rs = gain / loss
            if not pd.isna(rs.iloc[-1]):
                metrics['rsi'] = 100 - (100 / (1 + rs.iloc[-1]))
    except Exception as e:
        print(f"Error calculating metrics: {str(e)}")
    
    return metrics

def create_stock_visualization(data: pd.DataFrame, title: str, xlabel: str = "Date", ylabel: str = "Price") -> plt.Figure:
    """Create enhanced stock visualization with technical indicators."""
    try:
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), height_ratios=[3, 1])
        
        if isinstance(data, pd.Series):
            data = pd.DataFrame({'Close': data})
        
        if 'Close' not in data.columns:
            raise ValueError("Data must contain 'Close' column")
        
        # Plot price and moving averages
        ax1.plot(data.index, data['Close'], label='Close Price')
        
        # Only add moving averages if we have enough data points
        if len(data) >= 50:
            ax1.plot(data.index, data['Close'].rolling(window=50).mean(), label='50-day MA')
        if len(data) >= 200:
            ax1.plot(data.index, data['Close'].rolling(window=200).mean(), label='200-day MA')
        
        ax1.set_title(title)
        ax1.set_ylabel(ylabel)
        ax1.grid(True)
        ax1.legend()
        
        # Plot volume if available
        if 'Volume' in data.columns:
            price_change = data['Close'].diff()
            colors = ['green' if pc >= 0 else 'red' for pc in price_change]
            ax2.bar(data.index, data['Volume'], color=colors, alpha=0.5)
            ax2.set_xlabel(xlabel)
            ax2.set_ylabel('Volume')
            ax2.grid(True)
        
        plt.tight_layout()
        return fig
    except Exception as e:
        print(f"Error in visualization: {str(e)}")
        # Create a simple error figure
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.text(0.5, 0.5, f"Error creating visualization: {str(e)}", 
                ha='center', va='center')
        ax.axis('off')
        return fig

class FinancialAnalysis:
    def __init__(self):
        self.client = setup_client()
        
    def evaluate_report(self, report: str) -> Dict:
        """Evaluate the quality of a generated report."""
        evaluation_prompt = f"""Please evaluate the following financial report according to the template:

Report:
{report}

Template:
{EVALUATION_TEMPLATE}"""
        
        evaluation_response = generate_completion(evaluation_prompt)
        return parse_evaluation(evaluation_response)
    
    def validate_financial_data(self, data: Dict) -> bool:
        """Validate financial data for consistency and completeness."""
        required_fields = ['revenue', 'profit_margins', 'cash_flow', 'growth_rate']
        return all(field in data for field in required_fields)
    
    def calculate_financial_metrics(self, data: Dict) -> Dict:
        """Calculate key financial metrics from raw data."""
        metrics = {}
        
        if 'revenue' in data and 'costs' in data:
            metrics['gross_margin'] = (data['revenue'] - data['costs']) / data['revenue']
            
        if 'net_income' in data and 'revenue' in data:
            metrics['net_margin'] = data['net_income'] / data['revenue']
            
        if 'debt' in data and 'equity' in data:
            metrics['debt_to_equity'] = data['debt'] / data['equity']
            
        return metrics
    
    def generate_market_analysis(self, company: str, industry: str, timeframe: str) -> Dict:
        """Generate comprehensive market analysis with evaluation."""
        prompt = MARKET_TRENDS_PROMPT.format(
            company=company,
            industry=industry,
            timeframe=timeframe
        )
        
        report = generate_completion(prompt)
        evaluation = self.evaluate_report(report)
        
        return {
            'report': report,
            'evaluation': evaluation,
            'timestamp': datetime.now().isoformat()
        }
    
    def generate_financial_forecast(self, company: str, timeframe: str, metrics: str) -> Dict:
        """Generate financial forecast with evaluation."""
        prompt = FINANCIAL_PROJECTIONS_PROMPT.format(
            company=company,
            timeframe=timeframe,
            metrics=metrics
        )
        
        report = generate_completion(prompt)
        evaluation = self.evaluate_report(report)
        
        return {
            'report': report,
            'evaluation': evaluation,
            'timestamp': datetime.now().isoformat()
        }
    
    def generate_investment_advice(self, company: str, risk_profile: str, investment_horizon: str) -> Dict:
        """Generate investment recommendations with evaluation."""
        prompt = INVESTMENT_RECOMMENDATIONS_PROMPT.format(
            company=company,
            risk_profile=risk_profile,
            investment_horizon=investment_horizon
        )
        
        report = generate_completion(prompt)
        evaluation = self.evaluate_report(report)
        
        return {
            'report': report,
            'evaluation': evaluation,
            'timestamp': datetime.now().isoformat()
        }

def parse_evaluation(evaluation_text: str) -> Dict:
    """Parse evaluation response into structured format."""
    scores = {}
    improvements = []
    checklist = {}
    
    # Extract scores
    score_pattern = r'(\d+)\. (\w+ Score) \(1-10\): (\d+)'
    for match in re.finditer(score_pattern, evaluation_text):
        scores[match.group(2)] = int(match.group(3))
    
    # Extract improvements
    improvements_pattern = r'\[IMPROVEMENT AREAS\](.*?)\[VERIFICATION CHECKLIST\]'
    improvements_match = re.search(improvements_pattern, evaluation_text, re.DOTALL)
    if improvements_match:
        improvements = [imp.strip() for imp in improvements_match.group(1).split('\n') if imp.strip()]
    
    # Extract checklist items
    checklist_pattern = r'□ (.*?)(?=□|\Z)'
    for match in re.finditer(checklist_pattern, evaluation_text, re.DOTALL):
        item = match.group(1).strip()
        checklist[item] = True
    
    return {
        'scores': scores,
        'improvements': improvements,
        'checklist': checklist
    } 