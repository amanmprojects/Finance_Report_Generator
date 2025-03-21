import streamlit as st
import pandas as pd
from utils import (
    FinancialAnalysis,
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
    
    try:
        # Market Trends Analysis
        market_cap = 100.0  # Default value
        geographic_focus = "North America, Europe"  # Default value
        
        reports['market_trends'] = financial_analyzer.generate_market_analysis(
            company=company,
            industry=industry,
            timeframe=timeframe,
            market_cap=market_cap,
            geographic_focus=geographic_focus
        )

        # Financial Projections
        metrics = "Revenue, EBITDA, Net Income, Operating Cash Flow"
        reports['financial_projections'] = financial_analyzer.generate_financial_forecast(
            company=company,
            timeframe=timeframe,
            metrics=metrics
        )

        # Investment Recommendations
        reports['investment_recommendations'] = financial_analyzer.generate_investment_advice(
            company=company,
            risk_profile=risk_profile,
            investment_horizon=investment_horizon
        )

        reports['success'] = True
    except Exception as e:
        reports['success'] = False
        reports['error'] = str(e)

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
                if all_reports.get('success', False):
                    st.success("✅ Analysis complete! View results below.")
                else:
                    st.error(f"Error generating reports: {all_reports.get('error', 'Unknown error')}")

        # Main content - Analysis tab
        tab1 = st.tabs([
            "📊 Comprehensive Analysis"
        ])[0]

        # Only show content in tabs if reports have been generated
        if 'all_reports' in locals() and all_reports.get('success', False):
            with tab1:
                # Market Trends Section
                st.header("Market Trends Analysis")
                st.write(all_reports['market_trends']['report'])
                st.divider()
                display_evaluation_metrics(all_reports['market_trends'].get('evaluation', {}))
                
                # Visualization for Market Trends
                mock_data = generate_mock_data()
                fig = create_stock_visualization(
                    mock_data['historical_data'],
                    f"{company} Stock Price and Volume",
                    "Date",
                    "Price ($)"
                )
                st.pyplot(fig)
                
                # Financial Projections Section
                st.header("Financial Projections")
                st.write(all_reports['financial_projections']['report'])
                st.divider()
                display_evaluation_metrics(all_reports['financial_projections'].get('evaluation', {}))
                
                # Visualization for Financial Projections
                fig = create_financial_visualization(
                    mock_data['financial_data'],
                    f"{company} Financial Projections",
                    "Date",
                    "Amount ($)"
                )
                st.pyplot(fig)
                
                # Investment Recommendations Section
                st.header("Investment Recommendations")
                st.write(all_reports['investment_recommendations']['report'])
                st.divider()
                display_evaluation_metrics(all_reports['investment_recommendations'].get('evaluation', {}))

    except Exception as e:
        st.error(f"Application error: {str(e)}")

if __name__ == "__main__":
    main() 