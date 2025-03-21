# Import all prompts from the original prompts.py
from prompts import (
    SYSTEM_CONTEXT,
    MARKET_TRENDS_PROMPT,
    FINANCIAL_PROJECTIONS_PROMPT,
    INVESTMENT_RECOMMENDATIONS_PROMPT,
    EVALUATION_TEMPLATE
)

# Hindi Translations
HINDI_SYSTEM_CONTEXT = """आप एक एलीट वित्तीय विश्लेषक AI हैं जिसमें मात्रात्मक वित्त, व्यवहारिक अर्थशास्त्र और उन्नत बाजार माइक्रोस्ट्रक्चर विश्लेषण में विशेषज्ञता है।
आपका विश्लेषण मशीन लर्निंग मॉडल, मोंटे कार्लो सिमुलेशन और रीयल-टाइम मार्केट सेंटीमेंट एनालिसिस सहित अत्याधुनिक पद्धतियों को शामिल करता है।
आप कड़े सांख्यिकीय सत्यापन और क्रॉस-मार्केट सहसंबंध विश्लेषण द्वारा समर्थित संस्थागत-ग्रेड अंतर्दृष्टि प्रदान करते हैं।"""

HINDI_MARKET_TRENDS_PROMPT = """[संदर्भ]
कंपनी: {company}
उद्योग: {industry}
समय सीमा: {timeframe}
बाजार पूंजीकरण: {market_cap}
भौगोलिक फोकस: {geographic_focus}

[कार्य]
उन्नत विश्लेषणात्मक ढांचे को शामिल करते हुए एक व्यापक बाजार रुझान विश्लेषण रिपोर्ट तैयार करें:

1. कार्यकारी सारांश
   - रणनीतिक मोड़ बिंदु
   - अल्फा जनरेशन के अवसर
   - जोखिम-समायोजित रिटर्न क्षमता
   - बाजार व्यवस्था वर्गीकरण"""

HINDI_FINANCIAL_PROJECTIONS_PROMPT = """[संदर्भ]
कंपनी: {company}
समय सीमा: {timeframe}
मेट्रिक्स: {metrics}
ऐतिहासिक डेटा रेंज: {historical_range}
विश्वास स्तर: {confidence_level}

[कार्य]
उन्नत मॉडलिंग तकनीकों का उपयोग करके व्यापक वित्तीय अनुमान तैयार करें:

1. वित्तीय सारांश
   - मुख्य मूल्य चालक पहचान
   - मोंटे कार्लो सिमुलेशन परिणाम
   - परिदृश्य-आधारित अनुमान
   - संवेदनशीलता विश्लेषण मैट्रिक्स"""

HINDI_INVESTMENT_RECOMMENDATIONS_PROMPT = """[संदर्भ]
कंपनी: {company}
जोखिम प्रोफाइल: {risk_profile}
निवेश क्षितिज: {investment_horizon}
पोर्टफोलियो संदर्भ: {portfolio_context}
बाजार व्यवस्था: {market_regime}

[कार्य]
उन्नत पोर्टफोलियो सिद्धांत को शामिल करते हुए संस्थागत-ग्रेड निवेश सिफारिशें प्रदान करें:

1. निवेश सारांश
   - अल्फा जनरेशन रणनीति
   - जोखिम-समायोजित रिटर्न प्रोफाइल
   - पोर्टफोलियो अनुकूलन प्रभाव
   - बाजार समय निर्धारण विचार
   - पोजीशन साइजिंग पद्धति"""

HINDI_EVALUATION_TEMPLATE = """[रिपोर्ट मूल्यांकन]
1. विश्लेषणात्मक कठोरता स्कोर (1-10):
2. रणनीतिक गहराई स्कोर (1-10):
3. कार्यान्वयन व्यवहार्यता स्कोर (1-10):
4. जोखिम प्रबंधन स्कोर (1-10):
5. नवाचार स्कोर (1-10):
6. समग्र उत्कृष्टता स्कोर (1-10):"""

# Marathi Translations
MARATHI_SYSTEM_CONTEXT = """तुम्ही एक एलीट फायनान्शियल अॅनालिस्ट AI आहात ज्यामध्ये क्वांटिटेटिव्ह फायनान्स, बिहेव्हियरल इकॉनॉमिक्स आणि अॅडव्हान्स्ड मार्केट मायक्रोस्ट्रक्चर अॅनालिसिसमध्ये विशेषज्ञता आहे।
तुमचे विश्लेषण मशीन लर्निंग मॉडेल्स, मोंटे कार्लो सिम्युलेशन्स आणि रिअल-टाइम मार्केट सेंटिमेंट अॅनालिसिस यासारख्या अत्याधुनिक पद्धतींचा समावेश करते।
तुम्ही कठोर सांख्यिकीय वैधता आणि क्रॉस-मार्केट कोरिलेशन अॅनालिसिसद्वारे समर्थित इन्स्टिट्यूशनल-ग्रेड इनसाइट्स प्रदान करता."""

MARATHI_MARKET_TRENDS_PROMPT = """[संदर्भ]
कंपनी: {company}
उद्योग: {industry}
कालावधी: {timeframe}
मार्केट कॅप: {market_cap}
भौगोलिक फोकस: {geographic_focus}

[कार्य]
प्रगत विश्लेषणात्मक फ्रेमवर्क समाविष्ट करून सर्वसमावेशक मार्केट ट्रेंड्स अॅनालिसिस रिपोर्ट तयार करा:

1. कार्यकारी सारांश
   - धोरणात्मक वळण बिंदू
   - अल्फा जनरेशन संधी
   - जोखीम-समायोजित परतावा क्षमता
   - मार्केट रेजिम वर्गीकरण"""

MARATHI_FINANCIAL_PROJECTIONS_PROMPT = """[संदर्भ]
कंपनी: {company}
कालावधी: {timeframe}
मेट्रिक्स: {metrics}
ऐतिहासिक डेटा रेंज: {historical_range}
विश्वास पातळी: {confidence_level}

[कार्य]
प्रगत मॉडेलिंग तंत्रांचा वापर करून सर्वसमावेशक आर्थिक अंदाज तयार करा:

1. आर्थिक सारांश
   - मुख्य मूल्य ड्रायव्हर्स ओळख
   - मोंटे कार्लो सिम्युलेशन निकाल
   - सिनारिओ-आधारित प्रोजेक्शन्स
   - संवेदनशीलता विश्लेषण मॅट्रिक्स"""

MARATHI_INVESTMENT_RECOMMENDATIONS_PROMPT = """[संदर्भ]
कंपनी: {company}
रिस्क प्रोफाइल: {risk_profile}
गुंतवणूक कालावधी: {investment_horizon}
पोर्टफोलिओ संदर्भ: {portfolio_context}
मार्केट रेजिम: {market_regime}

[कार्य]
प्रगत पोर्टफोलिओ थिअरी समाविष्ट करून इन्स्टिट्यूशनल-ग्रेड गुंतवणूक शिफारसी प्रदान करा:

1. गुंतवणूक सारांश
   - अल्फा जनरेशन स्ट्रॅटेजी
   - रिस्क-अॅडजस्टेड रिटर्न प्रोफाइल
   - पोर्टफोलिओ ऑप्टिमायझेशन इम्पॅक्ट
   - मार्केट टायमिंग कन्सिडरेशन्स
   - पोझिशन साइझिंग मेथडॉलॉजी"""

MARATHI_EVALUATION_TEMPLATE = """[अहवाल मूल्यांकन]
1. विश्लेषणात्मक सखोलता स्कोर (1-10):
2. धोरणात्मक खोली स्कोर (1-10):
3. अंमलबजावणी व्यवहार्यता स्कोर (1-10):
4. जोखीम व्यवस्थापन स्कोर (1-10):
5. नवकल्पना स्कोर (1-10):
6. एकूण उत्कृष्टता स्कोर (1-10):"""

# UI Translations
UI_TRANSLATIONS = {
    "English": {
        "title": "AI-Generated Financial Forecasting and Analysis Report",
        "generate_button": "Generate Complete Analysis Report",
        "company_name": "Company Name",
        "industry": "Industry",
        "timeframe": "Analysis Timeframe",
        "risk_profile": "Risk Profile",
        "investment_horizon": "Investment Horizon",
        "loading": "🔄 Generating comprehensive analysis report...",
        "success": "✅ Analysis complete! View results below.",
        "error": "Error generating reports: {}",
        "input_parameters": "Input Parameters",
        "select_language": "Select Language",
        "company_information": "Company Information",
        "analysis_parameters": "Analysis Parameters",
        "investment_profile": "Investment Profile",
        "powered_by": "Powered by Together AI's DeepSeek-R1 model",
        "comprehensive_analysis": "📊 Comprehensive Analysis",
        "market_trends_analysis": "Market Trends Analysis",
        "financial_projections": "Financial Projections",
        "investment_recommendations": "Investment Recommendations",
        "quality_scores": "Quality Scores",
        "improvement_areas": "Areas for Improvement",
        "error_displaying_metrics": "Error displaying metrics",
        "current_price": "Current Price",
        "market_cap": "Market Cap",
        "volume": "Volume",
        "rsi": "RSI",
        "technical_indicators": "Technical Indicators",
        "sma_50": "50-day MA",
        "sma_200": "200-day MA",
        "volatility": "Volatility",
        "stock_price_and_volume": "Stock Price and Volume",
        "date": "Date",
        "price": "Price ($)",
        "amount": "Amount ($)",
        "close_price": "Close Price",
        "error_visualization": "Error creating visualization",
        "news_title": "Latest News",
        "news_publisher": "Publisher",
        "news_date": "Date",
        "news_link": "Read More"
    },
    "Hindi": {
        "title": "AI-जनित वित्तीय पूर्वानुमान और विश्लेषण रिपोर्ट",
        "generate_button": "पूर्ण विश्लेषण रिपोर्ट जनरेट करें",
        "company_name": "कंपनी का नाम",
        "industry": "उद्योग",
        "timeframe": "विश्लेषण समयसीमा",
        "risk_profile": "जोखिम प्रोफाइल",
        "investment_horizon": "निवेश क्षितिज",
        "loading": "🔄 व्यापक विश्लेषण रिपोर्ट तैयार की जा रही है...",
        "success": "✅ विश्लेषण पूर्ण! नीचे परिणाम देखें।",
        "error": "रिपोर्ट जनरेट करने में त्रुटि: {}",
        "input_parameters": "इनपुट पैरामीटर्स",
        "select_language": "भाषा चुनें",
        "company_information": "कंपनी की जानकारी",
        "analysis_parameters": "विश्लेषण पैरामीटर्स",
        "investment_profile": "निवेश प्रोफाइल",
        "powered_by": "Together AI के DeepSeek-R1 मॉडल द्वारा संचालित",
        "comprehensive_analysis": "📊 व्यापक विश्लेषण",
        "market_trends_analysis": "बाजार रुझान विश्लेषण",
        "financial_projections": "वित्तीय पूर्वानुमान",
        "investment_recommendations": "निवेश सिफारिशें",
        "quality_scores": "गुणवत्ता स्कोर",
        "improvement_areas": "सुधार के क्षेत्र",
        "error_displaying_metrics": "मेट्रिक्स प्रदर्शित करने में त्रुटि",
        "current_price": "वर्तमान कीमत",
        "market_cap": "बाजार पूंजीकरण",
        "volume": "वॉल्यूम",
        "rsi": "आरएसआई",
        "technical_indicators": "तकनीकी संकेतक",
        "sma_50": "50-दिवसीय मूविंग एवरेज",
        "sma_200": "200-दिवसीय मूविंग एवरेज",
        "volatility": "वोलैटिलिटी",
        "stock_price_and_volume": "शेयर कीमत और वॉल्यूम",
        "date": "दिनांक",
        "price": "कीमत ($)",
        "amount": "राशि ($)",
        "close_price": "बंद कीमत",
        "error_visualization": "विज़ुअलाइज़ेशन बनाने में त्रुटि",
        "news_title": "ताज़ा समाचार",
        "news_publisher": "प्रकाशक",
        "news_date": "दिनांक",
        "news_link": "और पढ़ें"
    },
    "Marathi": {
        "title": "AI-जनरेटेड फायनान्शियल फोरकास्टिंग आणि अॅनालिसिस रिपोर्ट",
        "generate_button": "संपूर्ण विश्लेषण अहवाल तयार करा",
        "company_name": "कंपनीचे नाव",
        "industry": "उद्योग",
        "timeframe": "विश्लेषण कालावधी",
        "risk_profile": "रिस्क प्रोफाइल",
        "investment_horizon": "गुंतवणूक कालावधी",
        "loading": "🔄 सविस्तर विश्लेषण अहवाल तयार करत आहे...",
        "success": "✅ विश्लेषण पूर्ण! खाली निकाल पहा.",
        "error": "अहवाल तयार करताना त्रुटी: {}",
        "input_parameters": "इनपुट पॅरामीटर्स",
        "select_language": "भाषा निवडा",
        "company_information": "कंपनी माहिती",
        "analysis_parameters": "विश्लेषण पॅरामीटर्स",
        "investment_profile": "गुंतवणूक प्रोफाइल",
        "powered_by": "Together AI च्या DeepSeek-R1 मॉडेलद्वारे संचालित",
        "comprehensive_analysis": "📊 सर्वसमावेशक विश्लेषण",
        "market_trends_analysis": "बाजार रुझान विश्लेषण",
        "financial_projections": "आर्थिक अंदाज",
        "investment_recommendations": "गुंतवणूक शिफारसी",
        "quality_scores": "गुणवत्ता स्कोअर्स",
        "improvement_areas": "सुधारणा क्षेत्रे",
        "error_displaying_metrics": "मेट्रिक्स दर्शवण्यात त्रुटी",
        "current_price": "वर्तमान किंमत",
        "market_cap": "बाजार भांडवल",
        "volume": "व्हॉल्यूम",
        "rsi": "आरएसआय",
        "technical_indicators": "तांत्रिक निर्देशक",
        "sma_50": "50-दिवसीय मूव्हिंग एव्हरेज",
        "sma_200": "200-दिवसीय मूव्हिंग एव्हरेज",
        "volatility": "व्होलॅटिलिटी",
        "stock_price_and_volume": "शेअर किंमत आणि व्हॉल्यूम",
        "date": "दिनांक",
        "price": "किंमत ($)",
        "amount": "रक्कम ($)",
        "close_price": "बंद किंमत",
        "error_visualization": "व्हिज्युअलायझेशन तयार करताना त्रुटी",
        "news_title": "नवीनतम बातम्या",
        "news_publisher": "प्रकाशक",
        "news_date": "दिनांक",
        "news_link": "अधिक वाचा"
    }
}

# Language configuration
LANGUAGES = {
    "English": {
        "system_context": SYSTEM_CONTEXT,
        "market_trends": """[CONTEXT]
Company: {company}
Industry: {industry}
Timeframe: {timeframe}
Market Cap: {market_cap}
Geographic Focus: {geographic_focus}

Recent News Context:
{news_context}

[TASK]
Generate a comprehensive market trends analysis report incorporating advanced analytical frameworks and recent news:

1. **Executive Summary**
   - Strategic inflection points
   - Alpha generation opportunities
   - Risk-adjusted return potential
   - Market regime classification
   - Key news impact analysis

2. **Industry Analysis**
   - Total Addressable Market (TAM) analysis
   - Market penetration rates by segment
   - Industry concentration metrics (HHI)
   - Value chain analysis and margin distribution
   - Regulatory environment and compliance landscape
   - Recent industry news impact

3. **Growth Opportunities & Risks**
   - Porter's Five Forces analysis
   - Blue Ocean Strategy evaluation
   - Disruption potential assessment
   - ESG impact analysis
   - Geopolitical risk assessment
   - Supply chain resilience metrics
   - News-based risk factors

4. **Key Performance Metrics**
   - Industry-specific KPIs with peer benchmarking
   - Growth quality metrics (organic vs inorganic)
   - Return on Invested Capital (ROIC) analysis
   - Customer acquisition cost (CAC) trends
   - Lifetime value (LTV) analysis
   - Network effect quantification
   - News-driven performance indicators

5. **Future Outlook**
   - Scenario planning with probability weights
   - Technology adoption curves
   - Market structure evolution
   - Strategic optionality analysis
   - M&A landscape assessment
   - News-based future projections

[OUTPUT FORMAT]
- Executive-level presentation style
- Data visualization recommendations
- Statistical significance indicators
- Confidence intervals for projections
- Cross-reference to industry databases
- Actionable strategic initiatives
- News impact analysis

[EVALUATION CRITERIA]
- Quantitative rigor
- Strategic depth
- Forward-looking insights
- Risk-adjusted perspective
- Implementation feasibility
- News integration quality""",

        "financial_projections": """[CONTEXT]
Company: {company}
Timeframe: {timeframe}
Metrics to analyze: {metrics}
Historical Data Range: {historical_range}
Confidence Level: {confidence_level}

Recent News Context:
{news_context}

[TASK]
Generate comprehensive financial projections using advanced modeling techniques and recent news:

1. **Financial Summary**
   - Key value drivers identification
   - Monte Carlo simulation results
   - Scenario-based projections
   - Sensitivity analysis matrix
   - News impact on projections

2. **Revenue Analysis**
   - Revenue growth decomposition
   - Customer cohort analysis
   - Pricing power assessment
   - Market share trajectory
   - Geographic expansion impact
   - News-driven revenue factors

3. **Profitability Metrics**
   - Margin expansion levers
   - Operating leverage analysis
   - Cost structure optimization
   - Working capital efficiency
   - Asset utilization metrics
   - News impact on profitability

4. **Cash Flow Analysis**
   - Free cash flow projections
   - Capital expenditure optimization
   - Working capital requirements
   - Debt service capacity
   - Dividend sustainability
   - News-based cash flow factors

5. **Risk Assessment**
   - Value at Risk (VaR) analysis
   - Stress testing scenarios
   - Correlation risk assessment
   - Liquidity risk metrics
   - Counterparty risk evaluation
   - News-based risk factors

[OUTPUT FORMAT]
- Financial model specifications
- Key assumption documentation
- Statistical validation methods
- Risk-adjusted projections
- Quarterly and annual breakdowns
- Variance analysis framework
- News impact analysis

[EVALUATION CRITERIA]
- Model sophistication
- Assumption robustness
- Risk quantification
- Scenario coverage
- Implementation guidance
- News integration quality""",

        "investment_recommendations": """[CONTEXT]
Company: {company}
Risk Profile: {risk_profile}
Investment Horizon: {investment_horizon}
Portfolio Context: {portfolio_context}
Market Regime: {market_regime}

Recent News Context:
{news_context}

[TASK]
Provide institutional-grade investment recommendations incorporating advanced portfolio theory and recent news:

1. **Investment Summary**
   - Alpha generation strategy
   - Risk-adjusted return profile
   - Portfolio optimization impact
   - Market timing considerations
   - Position sizing methodology
   - News impact on strategy

2. **Valuation Analysis**
   - Multi-factor valuation model
   - DCF with real options
   - Relative valuation matrix
   - Sum-of-the-parts analysis
   - Intrinsic value calculation
   - News-based valuation adjustments

3. **Entry Strategy**
   - Technical analysis integration
   - Market microstructure analysis
   - Liquidity assessment
   - Transaction cost analysis
   - Implementation timing
   - News-based entry signals

4. **Risk Management**
   - Position sizing optimization
   - Stop-loss methodology
   - Portfolio correlation analysis
   - Hedging strategy design
   - Risk attribution framework
   - News-based risk factors

5. **Exit Strategy**
   - Multiple scenario analysis
   - Technical exit triggers
   - Fundamental exit criteria
   - Portfolio rebalancing rules
   - Tax optimization considerations
   - News-based exit signals

[OUTPUT FORMAT]
- Investment thesis documentation
- Risk management framework
- Position sizing calculator
- Monitoring dashboard
- Performance attribution model
- News impact analysis

[EVALUATION CRITERIA]
- Strategy sophistication
- Risk management robustness
- Implementation clarity
- Portfolio integration
- Performance tracking framework
- News integration quality""",

        "system_context": """You are an elite financial analyst AI with expertise in quantitative finance, behavioral economics, and advanced market microstructure analysis.
Your analysis incorporates cutting-edge methodologies including machine learning models, Monte Carlo simulations, and real-time market sentiment analysis.
You provide institutional-grade insights backed by rigorous statistical validation and cross-market correlation analysis.
You excel at integrating recent news and market events into your analysis to provide timely and relevant insights.""",

        "evaluation_template": """[REPORT EVALUATION]
1. **Analytical Rigor Score (1-10):**
2. **Strategic Depth Score (1-10):**
3. **Implementation Feasibility Score (1-10):**
4. **Risk Management Score (1-10):**
5. **Innovation Score (1-10):**
6. **Overall Excellence Score (1-10):**
7. **News Integration Score (1-10):**

[IMPROVEMENT AREAS]
1. Quantitative Enhancement Opportunities
2. Strategic Framework Refinements
3. Risk Management Optimizations
4. Implementation Efficiencies
5. Innovation Integration Points
6. News Analysis Improvements

[VERIFICATION CHECKLIST]
☐ Advanced Analytical Framework Implementation
☐ Comprehensive Risk Assessment
☐ Clear Strategic Recommendations
☐ Robust Implementation Plan
☐ Performance Tracking Framework
☐ Innovation Integration
☐ Cross-market Correlation Analysis
☐ Statistical Validation
☐ ESG Considerations
☐ Geopolitical Risk Assessment
☐ News Impact Analysis""",

        "ui": UI_TRANSLATIONS["English"]
    },
    "Hindi": {
        "system_context": HINDI_SYSTEM_CONTEXT,
        "market_trends": HINDI_MARKET_TRENDS_PROMPT,
        "financial_projections": HINDI_FINANCIAL_PROJECTIONS_PROMPT,
        "investment_recommendations": HINDI_INVESTMENT_RECOMMENDATIONS_PROMPT,
        "evaluation_template": HINDI_EVALUATION_TEMPLATE,
        "ui": UI_TRANSLATIONS["Hindi"]
    },
    "Marathi": {
        "system_context": MARATHI_SYSTEM_CONTEXT,
        "market_trends": MARATHI_MARKET_TRENDS_PROMPT,
        "financial_projections": MARATHI_FINANCIAL_PROJECTIONS_PROMPT,
        "investment_recommendations": MARATHI_INVESTMENT_RECOMMENDATIONS_PROMPT,
        "evaluation_template": MARATHI_EVALUATION_TEMPLATE,
        "ui": UI_TRANSLATIONS["Marathi"]
    }
} 