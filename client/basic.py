import requests
from getpass import getpass

import base64




username = input('Enter username: ')
password = getpass('Enter Password: ')

token_url = "http://127.0.0.1:8000/token/"

token_response = requests.post(token_url, json={"username":username, "password":password}).json()['token']


headers = {
    "Content-Type": "application/json",
    "Authorization": f'Token {token_response}',
}

post_url = "http://127.0.0.1:8000/posts/"



files = "C:/Users/user/Desktop/abnet/abnet/assets/img/portfolio/portfolio-details-2.jpg"



post_response = requests.post(post_url, headers=headers, json={
    "author": 1, "title": "We made it hard", "content": "success", "slug": "hollan","category": None,
    "status": "published"
})

# print(post_response.json())