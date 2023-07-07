import requests
import threading
from queue import Queue
from bs4 import BeautifulSoup

def get_url_title(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup.title.string.strip()
    except:
        pass

def worker():
    while True:
        url = url_queue.get()
        title = get_url_title(url)
        if title:
            print(f"{url} - {title}")
        url_queue.task_done()

# List of URLs to fetch titles from
urls = [
    "https://www.python.org/",
    "https://en.wikipedia.org/wiki/Main_Page",
    "https://www.youtube.com/",
    "https://www.reddit.com/",
    "https://www.amazon.com/",
    "https://www.nytimes.com/",
    "https://github.com/",
    "https://www.quora.com/",
    "https://www.spotify.com/",
    "https://www.cnn.com/",
    "https://www.facebook.com/", 
    "https://github.com/PranavVerma-droid/"
]

# Create a queue to hold the URLs
url_queue = Queue()

# Start a thread pool to fetch titles
for i in range(5):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

# Add URLs to the queue
for url in urls:
    url_queue.put(url)

# Wait for all URLs to be processed
url_queue.join()