import requests
api_url = 'http://jsonplaceholder.typicode.com/todos/1'

response = requests.post(api_url)
print(response.json)

todo = {
    "userId": 1,
    "id": 1,
    "title": 'Phatcharapuek Anurak' ,
    "complete": True
}

response = requests.put(api_url, json=todo)

print(response.json())
print(response.status_code)