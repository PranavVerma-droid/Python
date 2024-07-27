import requests
from bs4 import BeautifulSoup
import time
import json
from datetime import datetime
import sys

def scrape_subreddit(subreddit, sort='hot', limit=25, after=None):
    base_url = f"https://www.reddit.com/r/{subreddit}/{sort}.json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    params = {
        'limit': limit,
        'after': after
    }
    
    response = requests.get(base_url, headers=headers, params=params)
    
    if response.status_code != 200:
        print(f"Error: Status code {response.status_code}")
        return None
    
    data = response.json()
    posts = []
    
    for post in data['data']['children']:
        post_data = post['data']
        posts.append({
            'title': post_data['title'],
            'author': post_data['author'],
            'score': post_data['score'],
            'url': post_data['url'],
            'num_comments': post_data['num_comments'],
            'created_utc': post_data['created_utc']
        })
    
    return posts, data['data']['after']

def write_to_file(subreddit, posts, comments):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{subreddit}_{timestamp}.txt"
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"Subreddit: r/{subreddit}\n")
        file.write(f"Scraped on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        for i, post in enumerate(posts, 1):
            file.write(f"Post {i}:\n")
            file.write(f"Title: {post['title']}\n")
            file.write(f"Author: {post['author']}\n")
            file.write(f"Score: {post['score']}\n")
            file.write(f"URL: {post['url']}\n")
            file.write(f"Number of comments: {post['num_comments']}\n")
            file.write(f"Created UTC: {datetime.fromtimestamp(post['created_utc'])}\n")
            
            if post['url'] in comments:
                file.write("Top comments:\n")
                for j, comment in enumerate(comments[post['url']][:3], 1):
                    file.write(f"  Comment {j}:\n")
                    file.write(f"    Author: {comment['author']}\n")
                    file.write(f"    Comment: {comment['body'][:100]}...\n")
                    file.write(f"    Score: {comment['score']}\n")
                    file.write(f"    Created UTC: {datetime.fromtimestamp(comment['created_utc'])}\n")
            
            file.write("\n" + "-"*50 + "\n\n")
    
    print(f"Data has been written to {filename}")

def scrape_comments(post_url):
    url = f"{post_url}.json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error: Status code {response.status_code}")
        return None
    
    data = response.json()
    comments = []
    
    def extract_comments(comment_data):
        for comment in comment_data:
            if isinstance(comment, dict) and 'data' in comment:
                comment = comment['data']
                if 'body' in comment:
                    comments.append({
                        'author': comment.get('author', '[deleted]'),
                        'body': comment['body'],
                        'score': comment['score'],
                        'created_utc': comment['created_utc']
                    })
                if 'replies' in comment and isinstance(comment['replies'], dict):
                    extract_comments(comment['replies']['data']['children'])
    
    extract_comments(data[1]['data']['children'])
    return comments

if __name__ == "__main__":
    subreddit = "python"
    posts, after = scrape_subreddit(subreddit, sort='hot', limit=5)

    comments = {}
    try:
        for i, post in enumerate(posts, 1):
            print(f"Scraping comments for post {i} of {len(posts)}...")
            post_comments = scrape_comments(post['url'])
            if post_comments:
                comments[post['url']] = post_comments
            time.sleep(2)  # Be respectful with request frequency
        
        write_to_file(subreddit, posts, comments)
        print("Scraping completed successfully.")
    except KeyboardInterrupt:
        print("\nScraping interrupted by user. Saving data collected so far...")
        write_to_file(subreddit, posts, comments)
        print("Partial data saved. Exiting.")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Attempting to save partial data...")
        write_to_file(subreddit, posts, comments)
        print("Partial data saved. Exiting.")
        sys.exit(1)