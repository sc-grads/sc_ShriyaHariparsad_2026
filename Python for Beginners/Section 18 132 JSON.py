import json
file_path: str = 'data.json'

with open(file_path, 'r') as file:
    data: dict = json.load(file)
    print(data)

