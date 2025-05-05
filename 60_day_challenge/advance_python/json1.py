import json

person = 
'{"name": "John","age": 30,"city": "New York"}'

obj = json.loads(person)
print(obj)