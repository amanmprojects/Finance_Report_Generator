import streamlit as st
import pandas as pd
from utils import (
    generate_market_trends_report,
    generate_financial_projections,
    generate_investment_recommendations,
    create_trend_visualization,
    create_bar_chart,
    generate_mock_data,
    get_stock_data,
    create_stock_visualization
)

st.set_page_config(page_title="AI Financial Analysis", layout="wide")

def main():
    st.title("AI-Generated Financial Forecasting and Analysis Report")
    st.write("Powered by Together AI's DeepSeek-R1 model")

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
    tab1, tab2, tab3, tab4 = st.tabs(["Market Trends", "Financial Projections", "Investment Recommendations", "Real-Time Stock Data"])

    with tab1:
        st.header("Market Trends Analysis")
        if st.button("Generate Market Trends Report"):
            with st.spinner("Generating market trends report..."):
                report = generate_market_trends_report(company, industry, timeframe)
                st.write(report)
                
                # Mock data visualization
                mock_data = generate_mock_data()
                fig = create_trend_visualization(
                    mock_data['revenue'],
                    f"{company} Revenue Trend",
                    "Date",
                    "Revenue ($)"
                )
                st.pyplot(fig)

    with tab2:
        st.header("Financial Projections")
        if st.button("Generate Financial Projections"):
            with st.spinner("Generating financial projections..."):
                metrics = "Revenue, EBITDA, Net Income, Operating Cash Flow"
                projections = generate_financial_projections(company, timeframe, metrics)
                st.write(projections)
                
                # Mock data visualization
                mock_data = generate_mock_data()
                fig = create_bar_chart(
                    mock_data['profit'],
                    f"{company} Profit Projections",
                    "Date",
                    "Profit ($)"
                )
                st.pyplot(fig)

    with tab3:
        st.header("Investment Recommendations")
        if st.button("Generate Investment Recommendations"):
            with st.spinner("Generating investment recommendations..."):
                recommendations = generate_investment_recommendations(
                    company, risk_profile, investment_horizon
                )
                st.write(recommendations)

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
                stock_data = get_stock_data(ticker_symbol, period)
                
                if 'error' in stock_data:
                    st.error(f"Error fetching stock data: {stock_data['error']}")
                else:
                    # Display current stock information
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Current Price", f"${stock_data['current_price']:,.2f}")
                    with col2:
                        st.metric("Market Cap", f"${stock_data['market_cap']:,.0f}")
                    with col3:
                        st.metric("Volume", f"{stock_data['volume']:,.0f}")
                    
                    # Display stock price chart
                    fig = create_stock_visualization(
                        stock_data['historical_data'],
                        f"{ticker_symbol} Stock Price",
                        "Date",
                        "Price ($)"
                    )
                    st.pyplot(fig)
                    
                    # Display recent news
                    st.subheader("Recent News")
                    for news_item in stock_data['news']:
                        st.markdown(f"**{news_item['title']}**")
                        st.markdown(f"*{news_item['publisher']} - {news_item['link']}*")
                        st.markdown("---")

    # Model Critique Section
    st.sidebar.markdown("---")
    st.sidebar.header("Model Critique")
    st.sidebar.markdown("""
    ### Strengths
    - Comprehensive analysis across multiple financial aspects
    - Integration of market data and projections
    - Customizable risk profiles and timeframes
    
    ### Areas for Improvement
    - Add real-time market data integration
    - Implement historical performance analysis
    - Include competitor benchmarking
    - Add sentiment analysis from news and social media
    """)

if __name__ == "__main__":
    main() 