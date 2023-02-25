import requests

response = requests.post('http://127.0.0.1:5000/api/tasks', json={'task': 'First task'})
print(response.content)

response1 = requests.post('http://127.0.0.1:5000/api/tasks', json={'task': 'Another task'})
print(response1.content)

response2 = requests.get('http://127.0.0.1:5000/api/tasks')
print(response2.content)

response3 = requests.delete('http://127.0.0.1:5000/api/tasks/2')
print(response3.content)

response4 = requests.put('http://127.0.0.1:5000/api/tasks', json={'id': 1, 'task': 'Updated task.'})
print(response4.content)
