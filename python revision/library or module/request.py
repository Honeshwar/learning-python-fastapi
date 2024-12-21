'''
The requests module allows you to send HTTP requests using Python.

The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).

pip install requests
'''

import requests

url = 'https://www.google.com/search?q=python'

response = requests.get(url)
p = requests.post(url,json={"key":"value"},data={"key":"value"},headers={"key":"value"},params={"key":"value"})

print(response.status_code)

print(response.text.split('/')[0])