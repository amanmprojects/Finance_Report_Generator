import streamlit as st
import pandas as pd
from utils import (
    generate_market_trends_report,
    generate_financial_projections,
    generate_investment_recommendations,
    create_trend_visualization,
    create_bar_chart,
    generate_mock_data
)

st.set_page_config(page_title="AI Financial Analysis", layout="wide")

def main():
    st.title("AI-Generated Financial Forecasting and Analysis Report")
    st.write("Powered by Groq's deepseek-r1-distill-llama-70b model")

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
    tab1, tab2, tab3 = st.tabs(["Market Trends", "Financial Projections", "Investment Recommendations"])

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