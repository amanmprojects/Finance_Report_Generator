from langchain.prompts import PromptTemplate

MARKET_TRENDS_PROMPT = PromptTemplate(
    input_variables=["company", "industry", "timeframe"],
    template="""Analyze the current market trends for {company} in the {industry} industry over the next {timeframe}.
    Focus on:
    1. Key market drivers and challenges
    2. Competitive landscape analysis
    3. Growth opportunities and risks
    4. Industry-specific metrics and KPIs
    5. Regulatory environment impact
    
    Provide specific data points and actionable insights where possible."""
)

FINANCIAL_PROJECTIONS_PROMPT = PromptTemplate(
    input_variables=["company", "timeframe", "metrics"],
    template="""Generate financial projections for {company} over the next {timeframe}.
    Include analysis of:
    1. Revenue growth and profitability trends
    2. Key financial metrics: {metrics}
    3. Cash flow projections
    4. Balance sheet forecasts
    5. Risk factors and assumptions
    
    Provide specific numerical projections and confidence intervals where possible."""
)

INVESTMENT_RECOMMENDATIONS_PROMPT = PromptTemplate(
    input_variables=["company", "risk_profile", "investment_horizon"],
    template="""Provide investment recommendations for {company} based on:
    1. Risk profile: {risk_profile}
    2. Investment horizon: {investment_horizon}
    
    Include:
    1. Valuation analysis
    2. Risk-reward assessment
    3. Entry and exit points
    4. Portfolio allocation suggestions
    5. Alternative investment options
    
    Support recommendations with specific metrics and market data."""
) 