SYSTEM_CONTEXT = """You are an expert financial analyst AI with deep knowledge of market analysis, financial forecasting, and investment strategies. 
Provide detailed, data-driven analysis with specific metrics and actionable insights."""

MARKET_TRENDS_PROMPT = """[CONTEXT]
Company: {company}
Industry: {industry}
Timeframe: {timeframe}

[TASK]
Generate a comprehensive market trends analysis report with the following sections:

1. Executive Summary
   - Key findings and recommendations (2-3 bullet points)
   - Overall market sentiment

2. Industry Analysis
   - Market size and growth rate
   - Key market drivers
   - Competitive landscape (top 3-5 competitors)
   - Market share analysis

3. Growth Opportunities & Risks
   - SWOT analysis
   - Emerging trends
   - Potential disruptions
   - Regulatory impacts

4. Key Performance Metrics
   - Industry-specific KPIs
   - Benchmark comparisons
   - Growth metrics

5. Future Outlook
   - Market predictions
   - Technology trends
   - Strategic recommendations

[OUTPUT FORMAT]
- Use clear section headers
- Include specific numbers and percentages
- Provide data sources where applicable
- List actionable recommendations
- Keep total length to 1000-1500 words

[EVALUATION CRITERIA]
- Factual accuracy
- Data-driven insights
- Actionable recommendations
- Industry-specific relevance
- Clear structure and readability"""

FINANCIAL_PROJECTIONS_PROMPT = """[CONTEXT]
Company: {company}
Timeframe: {timeframe}
Metrics to analyze: {metrics}

[TASK]
Generate detailed financial projections with the following components:

1. Financial Summary
   - Key projections overview
   - Assumptions and methodology

2. Revenue Analysis
   - Growth rate projections
   - Revenue streams breakdown
   - Market size and penetration

3. Profitability Metrics
   - Gross margin trends
   - EBITDA projections
   - Net profit margins

4. Cash Flow Analysis
   - Operating cash flow
   - Investment requirements
   - Working capital needs

5. Risk Assessment
   - Sensitivity analysis
   - Key risk factors
   - Mitigation strategies

[OUTPUT FORMAT]
- Use tables for numerical data
- Include growth rates and percentages
- Provide confidence intervals
- List all assumptions clearly
- Include quarterly breakdowns

[EVALUATION CRITERIA]
- Mathematical accuracy
- Realistic assumptions
- Comprehensive coverage
- Clear methodology
- Risk consideration"""

INVESTMENT_RECOMMENDATIONS_PROMPT = """[CONTEXT]
Company: {company}
Risk Profile: {risk_profile}
Investment Horizon: {investment_horizon}

[TASK]
Provide comprehensive investment recommendations including:

1. Investment Summary
   - Key recommendation
   - Risk-reward profile
   - Investment timeline

2. Valuation Analysis
   - Current valuation metrics
   - Fair value estimation
   - Comparable analysis

3. Entry Strategy
   - Recommended entry points
   - Position sizing
   - Timing considerations

4. Risk Management
   - Stop-loss levels
   - Position monitoring
   - Diversification strategy

5. Exit Strategy
   - Target prices
   - Exit triggers
   - Rebalancing criteria

[OUTPUT FORMAT]
- Clear buy/hold/sell recommendation
- Specific price targets
- Risk management rules
- Timeline for actions
- Portfolio allocation percentages

[EVALUATION CRITERIA]
- Risk-reward alignment
- Strategy clarity
- Practical implementation
- Time horizon alignment
- Risk management robustness"""

EVALUATION_TEMPLATE = """[REPORT EVALUATION]
1. Accuracy Score (1-10):
2. Completeness Score (1-10):
3. Actionability Score (1-10):
4. Clarity Score (1-10):
5. Overall Quality Score (1-10):

[IMPROVEMENT AREAS]
1.
2.
3.

[VERIFICATION CHECKLIST]
□ Contains specific metrics and numbers
□ Includes actionable recommendations
□ Follows required format
□ Addresses all key sections
□ Provides clear conclusions""" 