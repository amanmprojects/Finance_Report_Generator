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
        "error": "Error generating reports: {}"
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
        "error": "रिपोर्ट जनरेट करने में त्रुटि: {}"
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
        "error": "अहवाल तयार करताना त्रुटी: {}"
    }
}

# Language configuration
LANGUAGES = {
    "English": {
        "system_context": SYSTEM_CONTEXT,
        "market_trends": MARKET_TRENDS_PROMPT,
        "financial_projections": FINANCIAL_PROJECTIONS_PROMPT,
        "investment_recommendations": INVESTMENT_RECOMMENDATIONS_PROMPT,
        "evaluation_template": EVALUATION_TEMPLATE,
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