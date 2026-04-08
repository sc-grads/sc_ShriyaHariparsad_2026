from typing import TextIO

file_path: str = 'info.txt'

try:
    with open(file_path, 'r') as f:
        text: str = f.read()

    print(text)
except FileNotFoundError:
    print(f'No file path found for: {file_path}')