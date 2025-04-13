# process.py
# Cleans text and makes summaries

from bs4 import BeautifulSoup
import re
import nltk

def clean_text(text):
    """Remove HTML and extra spaces from text."""
    text = BeautifulSoup(text, 'html.parser').get_text()
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def make_summary(text):
    """Create a short summary from text."""
    sentences = nltk.sent_tokenize(text)
    if not sentences:
        return ""
    summary = sentences[0][:100]
    if len(sentences[0]) > 100:
        summary += "..."
    return summary