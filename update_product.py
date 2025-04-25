import requests

endpoint = "http://localhost:8000/api/product/3/"

data = {
    'name' : "Xiaomiiii",
    'price' : 290,
    'description' : "Mobile created by society Xiaomi",
    'email': 'xiaomi@gmail.com'
}

response = requests.put(endpoint, json=data)

print(response.json())

print(response.status_code)