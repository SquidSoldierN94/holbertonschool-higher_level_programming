"""
task_02_requests.py

This script uses the requests library to interact with the JSONPlaceholder API.
It includes two functions:
1. fetch_and_print_posts: Fetches posts and prints their titles.
2. fetch_and_save_posts: Fetches posts and saves them to a CSV file.

Required Libraries:
- requests: For making HTTP requests.
- csv: For handling CSV file operations.
"""

import requests
import csv

def fetch_and_print_posts():
    """
    Fetches posts from the JSONPlaceholder API and prints their titles.

    This function sends a GET request to the API and checks the status code 
    of the response. If the request is successful (status code 200), 
    it parses the JSON response and iterates through the list of posts, 
    printing the title of each post.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    print(f'Status Code: {response.status_code}')
    
    if response.status_code == 200:
        posts = response.json()
        
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """
    Fetches posts from the JSONPlaceholder API and saves them to a CSV file.

    This function sends a GET request to the API and checks the status code 
    of the response. If the request is successful (status code 200), 
    it parses the JSON response and structures the data into a list of 
    dictionaries. Each dictionary represents a post with keys for 
    'id', 'title', and 'body'. Finally, it writes this data to a 
    CSV file named 'posts.csv'.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    if response.status_code == 200:
        posts = response.json()
        
        posts_data = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]
        
        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(posts_data)

if __name__ == '__main__':
    """
    This block executes the functions when the script is run directly.
    It calls both fetch_and_print_posts and fetch_and_save_posts 
    to demonstrate fetching and processing posts from the API.
    """
    fetch_and_print_posts()
    fetch_and_save_posts()
