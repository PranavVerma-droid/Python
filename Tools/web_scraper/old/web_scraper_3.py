import requests
import time
import csv
from datetime import datetime
import sys

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

def write_to_csv(post, comments, csv_writer):
    post_row = [
        post['title'],
        post['author'],
        post['score'],
        post['url'],
        post['num_comments'],
        datetime.fromtimestamp(post['created_utc']),
        post['selftext']
    ]
    
    for i in range(7):
        if i < len(comments):
            comment = comments[i]
            post_row.extend([
                comment['author'],
                comment['body'],
                comment['score'],
                datetime.fromtimestamp(comment['created_utc'])
            ])
        else:
            post_row.extend(['', '', '', ''])
    
    csv_writer.writerow(post_row)

def main():
    subreddit = "python"  # Change this to the subreddit you want to scrape
    after = None
    
    csv_filename = f"{subreddit}_posts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        
        # Write the header
        header = ['Title', 'Author', 'Score', 'URL', 'Number of Comments', 'Created UTC', 'Post Content']
        for i in range(1, 8):
            header.extend([f'Comment {i} Author', f'Comment {i} Content', f'Comment {i} Score', f'Comment {i} Created UTC'])
        csv_writer.writerow(header)
        
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
                    
                    write_to_csv(post, comments, csv_writer)
                    csvfile.flush()  # Ensure data is written to file
                    
                    time.sleep(5)  # Wait for 5 seconds between posts
                
                print("Waiting before fetching the next post...")
                time.sleep(10)  # Wait for 10 seconds before fetching the next post
                
            except KeyboardInterrupt:
                print("\nScraping interrupted by user. Exiting.")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                print("Waiting before trying again...")
                time.sleep(60)  # Wait for 1 minute before trying again

    print(f"Data has been written to {csv_filename}")

if __name__ == "__main__":
    main()