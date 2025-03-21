# AI Financial Forecasting and Analysis Report

A Streamlit application that generates comprehensive financial analysis reports using Groq's deepseek-r1-distill-llama-70b model and Langchain.

## Features

- Market trends analysis
- Financial projections
- Investment recommendations
- Interactive visualizations
- Customizable parameters

## Prerequisites

- Python 3.8+
- Groq API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Groq API key:
```
GROQ_API_KEY=your_api_key_here
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Use the sidebar to input:
   - Company name
   - Industry
   - Analysis timeframe
   - Risk profile
   - Investment horizon

4. Click the respective buttons in each tab to generate:
   - Market trends report
   - Financial projections
   - Investment recommendations

## Project Structure

- `app.py`: Main Streamlit application
- `utils.py`: Helper functions for visualization and model interaction
- `prompts.py`: Langchain prompts for different analysis types
- `requirements.txt`: Project dependencies
- `.env`: Environment variables (create this file)

## Model Details

The application uses Groq's deepseek-r1-distill-llama-70b model through Langchain for generating financial analysis reports. The model provides:

- Market trend analysis
- Financial projections
- Investment recommendations

## Future Improvements

- Integration with real-time market data
- Historical performance analysis
- Competitor benchmarking
- Sentiment analysis from news and social media
- Export reports to PDF/Excel
- User authentication and saved reports 