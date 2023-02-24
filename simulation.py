import requests

response = requests.post('http://127.0.0.1:5000/api/tasks/add', json={'task': 'Third task'})
print(response.content)

response2 = requests.get('http://127.0.0.1:5000/api/tasks')
print(response2.content)

response3 = requests.delete('http://127.0.0.1:5000/api/tasks/delete/3')
print(response3.content)

response4 = requests.put('http://127.0.0.1:5000/api/tasks/update', json={'id': 1, 'task': 'Updated task details'})
print(response4.content)
