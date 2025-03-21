import streamlit as st
import pandas as pd
from utils import (
    FinancialAnalysis,
    get_stock_data,
    create_stock_visualization,
    create_financial_visualization,
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

def generate_all_reports(financial_analyzer, company, industry, timeframe, risk_profile, investment_horizon):
    """Generate all reports at once."""
    reports = {}
    
    # Market Trends Analysis
    try:
        market_cap = 100.0  # Default value
        geographic_focus = "North America, Europe"  # Default value
        
        reports['market_trends'] = financial_analyzer.generate_market_analysis(
            company=company,
            industry=industry,
            timeframe=timeframe,
            market_cap=market_cap,
            geographic_focus=geographic_focus
        )
    except Exception as e:
        reports['market_trends'] = {'error': str(e)}

    # Financial Projections
    try:
        metrics = "Revenue, EBITDA, Net Income, Operating Cash Flow"
        historical_range = "5 years"  # Default historical range
        confidence_level = 0.95  # Default confidence level
        
        reports['financial_projections'] = financial_analyzer.generate_financial_forecast(
            company=company,
            timeframe=timeframe,
            metrics=metrics,
            historical_range=historical_range,
            confidence_level=confidence_level
        )
    except Exception as e:
        reports['financial_projections'] = {'error': str(e)}

    # Investment Recommendations
    try:
        # Create a default portfolio context
        portfolio_context = {
            "current_holdings": [],
            "risk_tolerance": risk_profile.lower(),
            "investment_goals": investment_horizon.split(" ")[0].lower(),
            "market_outlook": "neutral"
        }
        
        market_regime = "normal"  # Default market regime
        
        reports['investment_recommendations'] = financial_analyzer.generate_investment_advice(
            company=company,
            risk_profile=risk_profile,
            investment_horizon=investment_horizon,
            portfolio_context=portfolio_context,
            market_regime=market_regime
        )
    except Exception as e:
        reports['investment_recommendations'] = {'error': str(e)}

    return reports

def main():
    st.title("AI-Generated Financial Forecasting and Analysis Report")
    st.write("Powered by Together AI's DeepSeek-R1 model")

    try:
        # Initialize Financial Analysis
        financial_analyzer = FinancialAnalysis()

        # Sidebar inputs
        with st.sidebar:
            st.header("Input Parameters")
            
            # Company Information
            st.subheader("Company Information")
            company = st.text_input("Company Name", "Apple")
            industry = st.selectbox(
                "Industry",
                ["Technology", "Healthcare", "Finance", "Retail", "Manufacturing"]
            )
            
            # Analysis Parameters
            st.subheader("Analysis Parameters")
            timeframe = st.selectbox(
                "Analysis Timeframe",
                ["6 months", "1 year", "2 years", "5 years"]
            )
            
            # Investment Profile
            st.subheader("Investment Profile")
            risk_profile = st.select_slider(
                "Risk Profile",
                options=["Conservative", "Moderate", "Aggressive"],
                value="Moderate"
            )
            investment_horizon = st.select_slider(
                "Investment Horizon",
                options=["Short-term (1-2 years)", "Medium-term (3-5 years)", "Long-term (5+ years)"],
                value="Medium-term (3-5 years)"
            )

        # Generate All Reports Button - Centered and prominent
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Generate Complete Analysis Report", type="primary", use_container_width=True):
                with st.spinner("🔄 Generating comprehensive analysis report..."):
                    all_reports = generate_all_reports(
                        financial_analyzer,
                        company,
                        industry,
                        timeframe,
                        risk_profile,
                        investment_horizon
                    )
                st.success("✅ Analysis complete! View results in the tabs below.")

        # Main content
        tab1, tab2, tab3, tab4 = st.tabs([
            "📈 Market Trends",
            "📊 Financial Projections",
            "💡 Investment Recommendations",
            "📱 Real-Time Stock Data"
        ])

        # Only show content in tabs if reports have been generated
        if 'all_reports' in locals():
            with tab1:
                st.header("Market Trends Analysis")
                if 'error' in all_reports['market_trends']:
                    st.error(f"Error in market trends analysis: {all_reports['market_trends']['error']}")
                else:
                    st.write(all_reports['market_trends']['report'])
                    st.divider()
                    display_evaluation_metrics(all_reports['market_trends'].get('evaluation', {}))
                    
                    # Visualization
                    mock_data = generate_mock_data()
                    fig = create_stock_visualization(
                        mock_data['historical_data'],
                        f"{company} Stock Price and Volume",
                        "Date",
                        "Price ($)"
                    )
                    st.pyplot(fig)

            with tab2:
                st.header("Financial Projections")
                if 'error' in all_reports['financial_projections']:
                    st.error(f"Error in financial projections: {all_reports['financial_projections']['error']}")
                else:
                    st.write(all_reports['financial_projections']['report'])
                    st.divider()
                    display_evaluation_metrics(all_reports['financial_projections'].get('evaluation', {}))
                    
                    # Visualization
                    mock_data = generate_mock_data()
                    fig = create_financial_visualization(
                        mock_data['financial_data'],
                        f"{company} Financial Projections",
                        "Date",
                        "Amount ($)"
                    )
                    st.pyplot(fig)

            with tab3:
                st.header("Investment Recommendations")
                if 'error' in all_reports['investment_recommendations']:
                    st.error(f"Error in investment recommendations: {all_reports['investment_recommendations']['error']}")
                else:
                    st.write(all_reports['investment_recommendations']['report'])
                    st.divider()
                    display_evaluation_metrics(all_reports['investment_recommendations'].get('evaluation', {}))

        with tab4:
            st.header("Real-Time Stock Data")
            col1, col2 = st.columns([2, 1])
            with col1:
                ticker_symbol = st.text_input("Enter Stock Ticker Symbol (e.g., AAPL for Apple)", "AAPL")
            with col2:
                period = st.selectbox(
                    "Select Time Period",
                    ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"],
                    index=5  # Default to 1y
                )
            
            if st.button("Fetch Stock Data", type="secondary", use_container_width=True):
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
                                with st.container():
                                    st.markdown(f"**{news_item['title']}**")
                                    st.markdown(f"*{news_item['publisher']} - {news_item['link']}*")
                                    st.markdown("---")
                        else:
                            st.error(f"Error fetching stock data: {stock_data.get('error', 'Unknown error')}")
                    except Exception as e:
                        st.error(f"Error processing stock data: {str(e)}")

        # Model Information
        st.sidebar.markdown("---")
        st.sidebar.header("ℹ️ Model Information")
        st.sidebar.markdown("""
        This financial analysis tool uses advanced AI to provide:
        - 📈 Market trend analysis
        - 📊 Financial projections
        - 💡 Investment recommendations
        - 📱 Real-time stock data analysis
        
        Each report is evaluated for:
        - ✓ Accuracy
        - ✓ Completeness
        - ✓ Actionability
        - ✓ Clarity
        """)
    except Exception as e:
        st.error(f"Application error: {str(e)}")

if __name__ == "__main__":
    main() 