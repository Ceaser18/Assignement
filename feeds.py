# Define RSS feeds for each category with updated finance feeds
RSS_FEEDS = {
    'general': ['http://feeds.bbci.co.uk/news/world/rss.xml', 'https://rss.nytimes.com/services/xml/rss/nyt/World.xml', 'http://feeds.reuters.com/reuters/topNews'],
    'technology': ['https://techcrunch.com/feed/', 'https://www.wired.com/feed/rss', 'https://www.technologyreview.com/feed/'],
    'finance': [
        'http://feeds.reuters.com/reuters/businessNews',  # Reuters Finance
        'https://www.ft.com/?format=rss',  # Financial Times
        'https://finance.yahoo.com/news/rss'  # Yahoo Finance
    ],
    'sports': ['https://www.espn.com/espn/rss/news', 'http://feeds.bbci.co.uk/sport/rss.xml', 'https://www.skysports.com/rss'],
    'entertainment': ['https://variety.com/feed/', 'https://www.hollywoodreporter.com/feed/', 'https://www.billboard.com/feed/'],
    'science': ['https://www.nasa.gov/rss/dyn/breaking_news.rss', 'https://www.sciencedaily.com/rss/all.xml', 'https://arstechnica.com/feed/']
}

# Define user personas with their interests and categories
USER_PERSONAS = {
    'Alex Parker': {'interests': ['AI', 'cybersecurity', 'blockchain', 'startups', 'programming'], 'categories': ['technology']},
    'Priya Sharma': {'interests': ['global markets', 'startups', 'fintech', 'cryptocurrency', 'economics'], 'categories': ['finance']},
    'Marco Rossi': {'interests': ['football', 'F1', 'NBA', 'olympic sports', 'esports'], 'categories': ['sports']},
    'Lisa Thompson': {'interests': ['movies', 'celebrity news', 'TV shows', 'music', 'books'], 'categories': ['entertainment']},
    'David Martinez': {'interests': ['space exploration', 'AI', 'biotech', 'physics', 'renewable energy'], 'categories': ['science', 'technology']}
}