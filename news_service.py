import os
import requests
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class BraveNewsService:
    def __init__(self):
        self.api_key = os.getenv("BRAVE_API_KEY")
        if not self.api_key:
            raise ValueError("BRAVE_API_KEY environment variable is not set")
        self.base_url = "https://api.search.brave.com/res/v1/web/search"

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
        Fetch company news using Brave Search API.
        
        Args:
            company (str): Company name to search for
            timeframe (str): Timeframe for news (6 months, 1 year, 2 years, 5 years)
            language (str): Language for news articles (default: English)
            
        Returns:
            List[Dict]: List of news articles with title, description, link, and published date
        """
        try:
            # Calculate date range
            days = self._get_timeframe_days(timeframe)
            end_date = datetime.now()
            start_date = end_date - timedelta(days=days)

            # Prepare search query
            query = f"{company} company news"
            
            # Prepare headers
            headers = {
                "Accept": "application/json",
                "X-Subscription-Token": self.api_key
            }

            # Prepare parameters
            params = {
                "q": query,
                "count": 10,  # Number of results to return
                "search_lang": language,
                "freshness": "d" + str(days),  # Filter by freshness in days
                "text_format": "plain"  # Get plain text for better processing
            }

            # Make API request
            response = requests.get(
                self.base_url,
                headers=headers,
                params=params
            )
            response.raise_for_status()

            # Parse response
            data = response.json()
            
            # Extract and format news articles
            news_articles = []
            for result in data.get("web", {}).get("results", []):
                article = {
                    "title": result.get("title", ""),
                    "description": result.get("description", ""),
                    "link": result.get("url", ""),
                    "published": result.get("published", ""),
                    "source": result.get("source", "")
                }
                news_articles.append(article)

            return news_articles

        except requests.exceptions.RequestException as e:
            print(f"Error fetching news from Brave Search: {str(e)}")
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