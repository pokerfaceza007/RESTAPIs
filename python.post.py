import requests
api_url = 'http://jsonplaceholder.typicode.com/todos'

todo = {
    "userId": 909,
    "id": 909,
    "title": 'Phatcharapuek Anurak' ,
    "complete": False
}

response = requests.post(api_url, json=todo)

print(response.json())
print(response.status_code)