import requests
import time
import json

now = int(time.time())
day_ago = now - 24 * 3600

# Fetch top stories of last 24 hours (points > 10)
url = f"https://hn.algolia.com/api/v1/search_by_date?tags=story&numericFilters=created_at_i>{day_ago},points>10&hitsPerPage=100"
try:
    r = requests.get(url, timeout=10)
    if r.status_code == 200:
        hits = r.json().get('hits', [])
        results = []
        for h in hits:
            results.append({
                'title': h.get('title'),
                'url': h.get('url') or f"https://news.ycombinator.com/item?id={h.get('objectID')}",
                'points': h.get('points'),
                'num_comments': h.get('num_comments'),
                'created_at': h.get('created_at'),
                'created_at_i': h.get('created_at_i'),
                'story_id': h.get('objectID'),
                'text': h.get('story_text') or ''
            })
        print(json.dumps(results[:40], indent=2))
except Exception as e:
    print(f"Error fetching top stories: {e}")
