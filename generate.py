# generate.py
# Creates and saves newsletters

from datetime import datetime
from process import make_summary

def create_newsletter(articles, user):
    """Write a Markdown newsletter for the user."""
    today = datetime.now().strftime("%Y-%m-%d")
    text = f"# Newsletter for {user}\n\n*Date: {today}*\n\n"
    
    if not articles:
        text += "No news found today.\n"
        return text
    
    text += "## Highlights\n\n"
    for article in articles[:2]:
        summary = make_summary(article['summary'])
        text += f"- **{article['title']}**: {summary} [Read]({article['link']})\n"
    
    categories = set(a['category'] for a in articles)
    for cat in categories:
        text += f"\n## {cat.title()} News\n\n"
        for article in [a for a in articles if a['category'] == cat]:
            summary = make_summary(article['summary'])
            text += f"### {article['title']}\n\n{summary}\n\n[Full Story]({article['link']})\n\n"
    
    return text

def save_newsletter(text, user):
    """Save the newsletter to a file."""
    filename = f"newsletter_{user.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.md"
    with open(filename, 'w') as f:
        f.write(text)
    return filename