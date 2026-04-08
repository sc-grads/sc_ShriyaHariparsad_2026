file_path: str = 'info.txt'

with open(file_path, 'a') as txt:
    txt.writelines(['Eggs\n', 'Ham\n', 'Spam\n'])


