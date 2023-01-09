import requests
api_url = 'http://jsonplaceholder.typicode.com/todos/1'
#api_url = 'https://api.github.com/users/pokerfaceza007'

response = requests.get(api_url)

print(response.json())
print(response.status_code)