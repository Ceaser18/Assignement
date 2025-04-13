# fetch.py
# Gets articles from RSS feeds

import feedparser
from feeds import RSS_FEEDS

def fetch_articles():
    """Fetch articles from all RSS feeds."""
    articles = []
    for category, sources in RSS_FEEDS.items():
        for source in sources:
            try:
                feed = feedparser.parse(source)
                print(f"Fetched {len(feed.entries)} articles from {source}")
                for entry in feed.entries[:10]:  # Limit to 10 articles
                    article = {
                        'title': entry.get('title', ''),
                        'link': entry.get('link', ''),
                        'summary': entry.get('summary', '') or entry.get('description', ''),
                        'category': category
                    }
                    articles.append(article)
            except Exception as e:
                print(f"Error with {source}: {e}")
    return articles