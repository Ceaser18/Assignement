# main.py
# Runs the newsletter generator

import nltk
from feeds import USERS
from fetch import fetch_articles
from personalize import personalize_articles
from generate import create_newsletter, save_newsletter

def main():
    # Setup NLTK resources
    nltk.download('punkt_tab')
    nltk.download('stopwords')
    nltk.download('wordnet')  # Added to fix LookupError
    
    # Get all articles
    print("Fetching articles...")
    articles = fetch_articles()
    
    # Create newsletters for each user
    for user in USERS:
        print(f"Generating newsletter for {user}...")
        user_articles = personalize_articles(articles, user)
        newsletter_text = create_newsletter(user_articles, user)
        filename = save_newsletter(newsletter_text, user)
        print(f"Saved as {filename}")

if __name__ == "__main__":
    main()