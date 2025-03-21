import os
import requests
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from bs4 import BeautifulSoup
import time
import json

class DuckDuckGoNewsService:
    def __init__(self):
        self.base_url = "https://api.duckduckgo.com/"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def _get_timeframe_days(self, timeframe: str) -> int:
        """Convert timeframe string to number of days."""
        timeframe_map = {
            "6 months": 180,
            "1 year": 365,
            "2 years": 730,
            "5 years": 1825
        }
        return timeframe_map.get(timeframe, 365)  # Default to 1 year if timeframe not found

    def fetch_company_news(self, company: str, timeframe: str, language: str = "English") -> List[Dict]:
        """
        Fetch company news using DuckDuckGo.
        
        Args:
            company (str): Company name to search for
            timeframe (str): Timeframe for news (6 months, 1 year, 2 years, 5 years)
            language (str): Language for news articles (default: English)
            
        Returns:
            List[Dict]: List of news articles with title, description, link, and published date
        """
        try:
            # Prepare search query with news-specific terms
            query = f"{company} company financial news stock market"
            print(f"\nSearching DuckDuckGo for: {query}")
            print(f"Timeframe: {timeframe}")
            print(f"Language: {language}")
            
            # Prepare parameters for news search
            params = {
                "q": query,
                "format": "json",
                "no_html": 1,
                "skip_disambig": 1,
                "no_redirect": 1,
                "t": "Finance",
                "ia": "web",  # Use web search
                "iax": 1,     # Enable instant answers
                "ia_web": 1,  # Enable web results
                "ia_news": 1  # Enable news results
            }

            print("\nMaking request to DuckDuckGo...")
            # Make API request
            response = requests.get(
                self.base_url,
                headers=self.headers,
                params=params
            )
            response.raise_for_status()

            print("\nParsing response...")
            data = response.json()
            
            # Extract news from the response
            news_articles = []
            
            # Try to get news from RelatedTopics
            if 'RelatedTopics' in data:
                for topic in data['RelatedTopics']:
                    if 'Text' in topic and 'FirstURL' in topic:
                        article = {
                            "title": topic['Text'].split(' - ')[0] if ' - ' in topic['Text'] else topic['Text'][:100],
                            "description": topic['Text'],
                            "link": topic['FirstURL'],
                            "published": datetime.now().isoformat(),
                            "source": topic['FirstURL'].split('/')[2] if len(topic['FirstURL'].split('/')) > 2 else "Unknown Source"
                        }
                        news_articles.append(article)
                        print(f"\nFound article:")
                        print(f"Title: {article['title']}")
                        print(f"Source: {article['source']}")
                        print(f"Link: {article['link']}")
                        print(f"Description: {article['description'][:100]}...")

            # If no news found in RelatedTopics, try Results
            if not news_articles and 'Results' in data:
                for result in data['Results']:
                    if 'Text' in result and 'FirstURL' in result:
                        article = {
                            "title": result['Text'].split(' - ')[0] if ' - ' in result['Text'] else result['Text'][:100],
                            "description": result['Text'],
                            "link": result['FirstURL'],
                            "published": datetime.now().isoformat(),
                            "source": result['FirstURL'].split('/')[2] if len(result['FirstURL'].split('/')) > 2 else "Unknown Source"
                        }
                        news_articles.append(article)
                        print(f"\nFound article:")
                        print(f"Title: {article['title']}")
                        print(f"Source: {article['source']}")
                        print(f"Link: {article['link']}")
                        print(f"Description: {article['description'][:100]}...")

            print(f"\nSuccessfully found {len(news_articles)} articles")
            
            # Add a small delay to be respectful to DuckDuckGo's servers
            time.sleep(1)
            
            return news_articles

        except requests.exceptions.RequestException as e:
            print(f"\nError fetching news from DuckDuckGo: {str(e)}")
            return []
        except json.JSONDecodeError as e:
            print(f"\nError parsing JSON response: {str(e)}")
            return []

    def format_news_for_prompt(self, news_articles: List[Dict]) -> str:
        """
        Format news articles into a string suitable for including in a prompt.
        
        Args:
            news_articles (List[Dict]): List of news articles
            
        Returns:
            str: Formatted news summary
        """
        if not news_articles:
            return "No recent news articles found."

        formatted_news = "Recent News Articles:\n\n"
        for article in news_articles:
            formatted_news += f"Title: {article['title']}\n"
            formatted_news += f"Source: {article['source']}\n"
            formatted_news += f"Date: {article['published']}\n"
            formatted_news += f"Summary: {article['description']}\n"
            formatted_news += f"Link: {article['link']}\n"
            formatted_news += "-" * 80 + "\n"

        return formatted_news 