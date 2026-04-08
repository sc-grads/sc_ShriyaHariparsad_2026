file_path: str = 'info.txt'

with open(file_path, 'r') as f:
    print(f.readline())
    print(f.readline())