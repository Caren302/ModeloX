import requests
import json 

uri = "http://0.0.0.0:11434/api/chat"

data = {
    "model": "llama3-8b-8192",
}

headers = {
    "Authorization": "Bearer X123"
}

response = requests.post(uri, json=data, headers=headers) 

print(response.text)