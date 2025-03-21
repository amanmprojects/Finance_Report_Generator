import streamlit as st
import pandas as pd
from utils import (
    FinancialAnalysis,
    get_stock_data,
    create_stock_visualization,
    generate_mock_data
)

st.set_page_config(page_title="AI Financial Analysis", layout="wide")

def display_evaluation_metrics(evaluation):
    """Display evaluation metrics in a structured format."""
    try:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Quality Scores")
            for metric, score in evaluation.get('scores', {}).items():
                st.metric(metric, f"{score}/10")
        
        with col2:
            st.subheader("Areas for Improvement")
            for improvement in evaluation.get('improvements', []):
                st.write(f"• {improvement}")
        
        st.subheader("Verification Checklist")
        for item in evaluation.get('checklist', {}):
            st.checkbox(item, value=True, disabled=True)
    except Exception as e:
        st.error(f"Error displaying evaluation metrics: {str(e)}")

def display_stock_metrics(stock_data):
    """Display stock metrics in a structured format."""
    try:
        # Display current stock information
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Current Price", f"${stock_data.get('current_price', 0):,.2f}")
        with col2:
            st.metric("Market Cap", f"${stock_data.get('market_cap', 0):,.0f}")
        with col3:
            st.metric("Volume", f"{stock_data.get('volume', 0):,.0f}")
        with col4:
            st.metric("RSI", f"{stock_data.get('metrics', {}).get('rsi', 0):.2f}")
        
        # Technical Indicators
        st.subheader("Technical Indicators")
        col1, col2, col3 = st.columns(3)
        metrics = stock_data.get('metrics', {})
        with col1:
            st.metric("50-day MA", f"${metrics.get('sma_50', 0):.2f}")
        with col2:
            st.metric("200-day MA", f"${metrics.get('sma_200', 0):.2f}")
        with col3:
            st.metric("Volatility", f"{metrics.get('volatility', 0):.2%}")
    except Exception as e:
        st.error(f"Error displaying stock metrics: {str(e)}")

def main():
    st.title("AI-Generated Financial Forecasting and Analysis Report")
    st.write("Powered by Together AI's DeepSeek-R1 model")

    try:
        # Initialize Financial Analysis
        financial_analyzer = FinancialAnalysis()

        # Sidebar inputs
        st.sidebar.header("Input Parameters")
        company = st.sidebar.text_input("Company Name", "Example Corp")
        industry = st.sidebar.selectbox(
            "Industry",
            ["Technology", "Healthcare", "Finance", "Retail", "Manufacturing"]
        )
        timeframe = st.sidebar.selectbox(
            "Analysis Timeframe",
            ["6 months", "1 year", "2 years", "5 years"]
        )
        risk_profile = st.sidebar.selectbox(
            "Risk Profile",
            ["Conservative", "Moderate", "Aggressive"]
        )
        investment_horizon = st.sidebar.selectbox(
            "Investment Horizon",
            ["Short-term (1-2 years)", "Medium-term (3-5 years)", "Long-term (5+ years)"]
        )

        # Main content
        tab1, tab2, tab3, tab4 = st.tabs([
            "Market Trends",
            "Financial Projections",
            "Investment Recommendations",
            "Real-Time Stock Data"
        ])

        with tab1:
            st.header("Market Trends Analysis")
            if st.button("Generate Market Trends Report"):
                with st.spinner("Generating market trends report..."):
                    try:
                        analysis = financial_analyzer.generate_market_analysis(
                            company=company,
                            industry=industry,
                            timeframe=timeframe
                        )
                        
                        if analysis.get('report'):
                            st.write(analysis['report'])
                            st.divider()
                            display_evaluation_metrics(analysis.get('evaluation', {}))
                            
                            # Visualization
                            mock_data = generate_mock_data()
                            fig = create_stock_visualization(
                                mock_data['revenue'],
                                f"{company} Revenue Trend",
                                "Date",
                                "Revenue ($)"
                            )
                            st.pyplot(fig)
                        else:
                            st.error("Failed to generate market trends report")
                    except Exception as e:
                        st.error(f"Error in market trends analysis: {str(e)}")

        with tab2:
            st.header("Financial Projections")
            if st.button("Generate Financial Projections"):
                with st.spinner("Generating financial projections..."):
                    try:
                        metrics = "Revenue, EBITDA, Net Income, Operating Cash Flow"
                        projections = financial_analyzer.generate_financial_forecast(
                            company=company,
                            timeframe=timeframe,
                            metrics=metrics
                        )
                        
                        if projections.get('report'):
                            st.write(projections['report'])
                            st.divider()
                            display_evaluation_metrics(projections.get('evaluation', {}))
                            
                            # Visualization
                            mock_data = generate_mock_data()
                            fig = create_stock_visualization(
                                mock_data['profit'],
                                f"{company} Profit Projections",
                                "Date",
                                "Profit ($)"
                            )
                            st.pyplot(fig)
                        else:
                            st.error("Failed to generate financial projections")
                    except Exception as e:
                        st.error(f"Error in financial projections: {str(e)}")

        with tab3:
            st.header("Investment Recommendations")
            if st.button("Generate Investment Recommendations"):
                with st.spinner("Generating investment recommendations..."):
                    try:
                        recommendations = financial_analyzer.generate_investment_advice(
                            company=company,
                            risk_profile=risk_profile,
                            investment_horizon=investment_horizon
                        )
                        
                        if recommendations.get('report'):
                            st.write(recommendations['report'])
                            st.divider()
                            display_evaluation_metrics(recommendations.get('evaluation', {}))
                        else:
                            st.error("Failed to generate investment recommendations")
                    except Exception as e:
                        st.error(f"Error in investment recommendations: {str(e)}")

        with tab4:
            st.header("Real-Time Stock Data")
            ticker_symbol = st.text_input("Enter Stock Ticker Symbol (e.g., AAPL for Apple)", "AAPL")
            period = st.selectbox(
                "Select Time Period",
                ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"],
                index=5  # Default to 1y
            )
            
            if st.button("Fetch Stock Data"):
                with st.spinner("Fetching real-time stock data..."):
                    try:
                        stock_data = get_stock_data(ticker_symbol, period)
                        
                        if stock_data.get('success', False):
                            display_stock_metrics(stock_data)
                            
                            # Display stock price chart
                            if 'historical_data' in stock_data:
                                fig = create_stock_visualization(
                                    stock_data['historical_data'],
                                    f"{ticker_symbol} Stock Price",
                                    "Date",
                                    "Price ($)"
                                )
                                st.pyplot(fig)
                            
                            # Display recent news
                            st.subheader("Recent News")
                            for news_item in stock_data.get('news', []):
                                st.markdown(f"**{news_item['title']}**")
                                st.markdown(f"*{news_item['publisher']} - {news_item['link']}*")
                                st.markdown("---")
                        else:
                            st.error(f"Error fetching stock data: {stock_data.get('error', 'Unknown error')}")
                    except Exception as e:
                        st.error(f"Error processing stock data: {str(e)}")

        # Model Information
        st.sidebar.markdown("---")
        st.sidebar.header("Model Information")
        st.sidebar.markdown("""
        This financial analysis tool uses advanced AI to provide:
        - Market trend analysis
        - Financial projections
        - Investment recommendations
        - Real-time stock data analysis
        
        Each report is evaluated for:
        - Accuracy
        - Completeness
        - Actionability
        - Clarity
        """)
    except Exception as e:
        st.error(f"Application error: {str(e)}")

if __name__ == "__main__":
    main() 