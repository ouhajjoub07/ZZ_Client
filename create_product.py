import requests

endpoint = "http://localhost:8000/api/product/"

data = {
    'name' : "tbyyyy",
    'price' : 29000,
    'description' : "tbyyy dod wow",
    'email':'tby@gmail.com',
}
# data2 = {
#     'name' : "Android",
#     'price' : 790,
#     'description' : "Mobile created by society Samsung",
# }

# response = requests.post(endpoint, json=data)
response = requests.post(endpoint, json=data)

print(response.json())

print(response.status_code)