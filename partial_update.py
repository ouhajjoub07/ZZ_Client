import requests

endpoint = "http://localhost:8000/api/product/3/"

data = {
    'price' : 390,
}

response = requests.patch(endpoint, json=data)

print(response.json())

print(response.status_code)