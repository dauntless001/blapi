'''
Test Api Via the console with the client, add the necessary parameters and url to use
'''

import requests
from getpass import getpass

username = input('Enter username: ')
password = getpass('Enter Password: ')

token_url = "http://127.0.0.1:8000/token/"

token_response = requests.post(token_url, json={"username":username, "password":password}).json()['token']


headers = {
    "Authorization": f'Token {token_response}',
}

post_url = "http://127.0.0.1:8000/posts/"


post_response = requests.post(post_url, headers=headers, json={
    "author": 1, "title": "We made it hard", "content": "success", "slug": "hollan","category": None,
    "status": "published", "post_image": [{"image":"./1.jpg"}]
})

print(post_response.json())