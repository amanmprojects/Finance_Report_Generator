import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os
from utils import (
    FinancialAnalysis,
    create_stock_visualization,
    create_financial_visualization,
    generate_mock_data,
    display_news_articles,
    setup_client
)
from translated_prompts import LANGUAGES, UI_TRANSLATIONS
import markdown
import pdfkit
import tempfile

st.set_page_config(page_title="AI Financial Analysis", layout="wide")

def display_stock_metrics(stock_data, language="English"):
    """Display stock metrics in a structured format."""
    try:
        # Display current stock information
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric(LANGUAGES[language]["ui"]["current_price"], f"${stock_data.get('current_price', 0):,.2f}")
        with col2:
            st.metric(LANGUAGES[language]["ui"]["market_cap"], f"${stock_data.get('market_cap', 0):,.0f}")
        with col3:
            st.metric(LANGUAGES[language]["ui"]["volume"], f"{stock_data.get('volume', 0):,.0f}")
        with col4:
            st.metric(LANGUAGES[language]["ui"]["rsi"], f"{stock_data.get('metrics', {}).get('rsi', 0):.2f}")
        
        # Technical Indicators
        st.subheader(LANGUAGES[language]["ui"]["technical_indicators"])
        col1, col2, col3 = st.columns(3)
        metrics = stock_data.get('metrics', {})
        with col1:
            st.metric(LANGUAGES[language]["ui"]["sma_50"], f"${metrics.get('sma_50', 0):.2f}")
        with col2:
            st.metric(LANGUAGES[language]["ui"]["sma_200"], f"${metrics.get('sma_200', 0):.2f}")
        with col3:
            st.metric(LANGUAGES[language]["ui"]["volatility"], f"{metrics.get('volatility', 0):.2%}")
    except Exception as e:
        st.error(f"{LANGUAGES[language]['ui']['error_displaying_metrics']}: {str(e)}")

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

def generate_pdf_report(all_reports, company, language="English"):
    """Generate a PDF report from the markdown content."""
    ui = UI_TRANSLATIONS[language]
    
    try:
        # Create markdown content
        markdown_content = f"""# {company} Financial Analysis Report
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## {ui["market_trends_analysis"]}
{all_reports['market_trends']['report']}

## {ui["financial_projections"]}
{all_reports['financial_projections']['report']}

## {ui["investment_recommendations"]}
{all_reports['investment_recommendations']['report']}
"""
        
        # Convert markdown to HTML
        html_content = markdown.markdown(markdown_content)
        
        # Create a temporary file for the PDF
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp_file:
            pdf_path = tmp_file.name
        
        # Configure wkhtmltopdf path (default Windows installation path)
        config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
        
        # Convert HTML to PDF
        pdfkit.from_string(html_content, pdf_path, configuration=config)
        
        return pdf_path
    except Exception as e:
        st.error(f"Error generating PDF: {str(e)}")
        st.info("Please make sure wkhtmltopdf is installed. You can download it from: https://wkhtmltopdf.org/downloads.html")
        return None

def main():
    # Initialize selected_language with default value
    selected_language = "English"
    
    # Sidebar inputs
    with st.sidebar:
        st.header(LANGUAGES[selected_language]["ui"]["input_parameters"])
        
        # Language Selection
        selected_language = st.selectbox(
            LANGUAGES[selected_language]["ui"]["select_language"],
            options=list(LANGUAGES.keys()),
            index=0
        )
        
        # Get UI translations for selected language
        ui = LANGUAGES[selected_language]["ui"]
        
        # Company Information
        st.subheader(ui["company_information"])
        company = st.text_input(ui["company_name"], "Apple")
        industry = st.selectbox(
            ui["industry"],
            ["Technology", "Healthcare", "Finance", "Retail", "Manufacturing"]
        )
        
        # Analysis Parameters
        st.subheader(ui["analysis_parameters"])
        timeframe = st.selectbox(
            ui["timeframe"],
            ["6 months", "1 year", "2 years", "5 years"]
        )
        
        # Investment Profile
        st.subheader(ui["investment_profile"])
        risk_profile = st.select_slider(
            ui["risk_profile"],
            options=["Conservative", "Moderate", "Aggressive"],
            value="Moderate"
        )
        investment_horizon = st.select_slider(
            ui["investment_horizon"],
            options=["Short-term (1-2 years)", "Medium-term (3-5 years)", "Long-term (5+ years)"],
            value="Medium-term (3-5 years)"
        )

        st.subheader("Model Settings")
        selected_model = st.selectbox(
            "Select Language Model",
            [
                "meta-llama/Llama-3.3-70B-Instruct-Turbo",
                "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
                "deepseek-ai/DeepSeek-R1",
                "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo"
            ],
            index=0  # Default to the first model
        )
        
        # Update the MODEL_NAME in the environment
        os.environ["MODEL_NAME"] = selected_model

    # Main content
    st.title(ui["title"])
    st.write(ui["powered_by"])

    # Initialize Financial Analysis with selected language
    financial_analyzer = FinancialAnalysis(language=selected_language)

    # Generate All Reports Button - Centered and prominent
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button(ui["generate_button"], type="primary", use_container_width=True):
            with st.spinner(ui["loading"]):
                all_reports = generate_all_reports(
                    financial_analyzer,
                    company,
                    industry,
                    timeframe,
                    risk_profile,
                    investment_horizon
                )
            if all_reports.get('success', False):
                st.success(ui["success"])
                
                # Generate PDF report
                pdf_path = generate_pdf_report(all_reports, company, selected_language)
                
                # Add download button for PDF
                with open(pdf_path, "rb") as pdf_file:
                    st.download_button(
                        label="📥 Download PDF Report",
                        data=pdf_file,
                        file_name=f"{company}_financial_report.pdf",
                        mime="application/pdf"
                    )
                
                # Clean up temporary file
                os.unlink(pdf_path)
            else:
                st.error(ui["error"].format(all_reports.get('error', 'Unknown error')))

    # Only show content in tabs if reports have been generated
    if 'all_reports' in locals() and all_reports.get('success', False):
        tab1, tab2, tab3 = st.tabs([
            ui["market_trends_analysis"],
            ui["financial_projections"],
            ui["investment_recommendations"]
        ])

        with tab1:
            # Market Trends Section
            st.header(ui["market_trends_analysis"])
            st.write(all_reports['market_trends']['report'])
            st.divider()
            display_news_articles(all_reports['market_trends'].get('news_articles', []), selected_language)
            
            # Visualization for Market Trends
            mock_data = generate_mock_data()
            fig = create_stock_visualization(
                mock_data['historical_data'],
                f"{company} {ui['stock_price_and_volume']}",
                ui["date"],
                ui["price"]
            )
            st.pyplot(fig)

        with tab2:
            # Financial Projections Section
            st.header(ui["financial_projections"])
            st.write(all_reports['financial_projections']['report'])
            st.divider()
            display_news_articles(all_reports['financial_projections'].get('news_articles', []), selected_language)
            
            # Visualization for Financial Projections
            fig = create_financial_visualization(
                mock_data['financial_data'],
                f"{company} {ui['financial_projections']}",
                ui["date"],
                ui["amount"]
            )
            st.pyplot(fig)

        with tab3:
            # Investment Recommendations Section
            st.header(ui["investment_recommendations"])
            st.write(all_reports['investment_recommendations']['report'])
            st.divider()
            display_news_articles(all_reports['investment_recommendations'].get('news_articles', []), selected_language)

if __name__ == "__main__":
    main() 