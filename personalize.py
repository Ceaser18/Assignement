# personalize.py
# Picks articles based on user interests

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from feeds import USERS
from process import clean_text

def personalize_articles(articles, user):
    """Select articles matching user's interests."""
    # Get user details
    user_interests = USERS[user]['interests']
    user_categories = USERS[user]['categories']
    
    # Filter by category
    relevant = [a for a in articles if a['category'] in user_categories]
    print(f"Found {len(relevant)} articles for {user}")
    
    if not relevant:
        return []
    
    # Prepare text for comparison
    texts = [clean_text(a['title'] + ' ' + a['summary']) for a in relevant]
    interest_text = ' '.join(user_interests)
    
    try:
        # Compare using TF-IDF
        comparer = TfidfVectorizer(stop_words='english')
        all_texts = texts + [interest_text]
        scores = comparer.fit_transform(all_texts)
        similarities = cosine_similarity(scores[-1:], scores[:-1])[0]
        
        # Rank articles
        ranked = list(zip(relevant, similarities))
        ranked.sort(key=lambda x: x[1], reverse=True)
        
        # Pick top articles or fallback
        picked = [article for article, score in ranked if score > 0.05]
        if not picked:
            print(f"No close matches for {user}, using top 5")
            picked = [article for article, _ in ranked[:5]]
        
        return picked[:5]
    except Exception as e:
        print(f"Comparison failed for {user}: {e}")
        return relevant[:5]