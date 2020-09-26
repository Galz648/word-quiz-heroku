import requests

url = 'http://0.0.0.0:5000/user'
user_data = {'email': 'postRequestEmail'}
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
x = requests.post(url, json = user_data, headers=headers)
print(x.json())
