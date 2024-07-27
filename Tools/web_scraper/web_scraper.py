import requests
import time
import json
from datetime import datetime
import sys
import os

platform = sys.platform

def scrape_subreddit(subreddit, sort='new', limit=1, after=None):
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
        return None, None
    
    data = response.json()
    posts = []
    
    for post in data['data']['children']:
        post_data = post['data']
        posts.append({
            'title': post_data['title'],
            'author': post_data['author'],
            'score': post_data['score'],
            'url': post_data['url'],
            'permalink': post_data['permalink'],
            'num_comments': post_data['num_comments'],
            'created_utc': post_data['created_utc'],
            'selftext': post_data['selftext']
        })
    
    return posts, data['data']['after']

def scrape_comments(permalink):
    url = f"https://www.reddit.com{permalink}.json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error: Status code {response.status_code}")
        return None
    
    data = response.json()
    comments = []
    
    if len(data) > 1 and 'data' in data[1] and 'children' in data[1]['data']:
        for comment in data[1]['data']['children']:
            if 'body' in comment['data']:
                comments.append({
                    'author': comment['data'].get('author', '[deleted]'),
                    'body': comment['data']['body'],
                    'score': comment['data']['score'],
                    'created_utc': comment['data']['created_utc']
                })
            if len(comments) == 7:
                break
    
    return comments

def write_to_file(post, comments, subreddit):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if platform == 'win32' or platform == 'cygwin' or platform == 'win64':
        folder_name = f"scrapes\scrape_{subreddit}"
    elif platform == 'linux':
        folder_name = f"scrapes/scrape_{subreddit}"
    else:
        print("Unsupported platform. Exiting.")
        sys.exit(1)

    
    # Check if the folder exists, if not, create it
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Created folder: {folder_name}")
    
    filename = os.path.join(folder_name, f"post_{timestamp}.txt")
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"Post Title: {post['title']}\n")
        file.write(f"Author: {post['author']}\n")
        file.write(f"Score: {post['score']}\n")
        file.write(f"URL: {post['url']}\n")
        file.write(f"Number of comments: {post['num_comments']}\n")
        file.write(f"Created UTC: {datetime.fromtimestamp(post['created_utc'])}\n\n")
        
        # Add the post content
        file.write("Post Content:\n")
        file.write(post['selftext'] if post['selftext'] else "[This post has no text content]")
        file.write("\n\n")
        
        if comments:
            file.write(f"Top {len(comments)} comments:\n")
            for i, comment in enumerate(comments, 1):
                file.write(f"Comment {i}:\n")
                file.write(f"  Author: {comment['author']}\n")
                file.write(f"  Comment: {comment['body']}\n")
                file.write(f"  Score: {comment['score']}\n")
                file.write(f"  Created UTC: {datetime.fromtimestamp(comment['created_utc'])}\n\n")
            
            if len(comments) < 7:
                file.write(f"Note: This post has only {len(comments)} comments at the time of scraping.\n")
        else:
            file.write("No comments found for this post.\n")
    
    print(f"Data has been written to {filename}")

def main():
    subreddit = str(input("Enter the subreddit to scrape: ")).strip()
     
    after = None
    
    while True:
        try:
            posts, after = scrape_subreddit(subreddit, sort='new', limit=1, after=after)
            
            if not posts:
                print("No more posts to scrape. Waiting before trying again...")
                time.sleep(60)  # Wait for 1 minute before trying again
                continue
            
            for post in posts:
                print(f"Scraping post: {post['title'][:50]}...")
                comments = scrape_comments(post['permalink'])
                
                if comments:
                    write_to_file(post, comments, subreddit)
                else:
                    print("No comments found for this post.")
                
                time.sleep(5)  # Wait for 5 seconds between posts
            
            print("Waiting before fetching the next post...")
            time.sleep(10)  # Wait for 10 seconds before fetching the next post
            
        except KeyboardInterrupt:
            print("\nScraping interrupted by user. Exiting.")
            sys.exit(0)
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Waiting before trying again...")
            time.sleep(60)  # Wait for 1 minute before trying again

if __name__ == "__main__":
    main()