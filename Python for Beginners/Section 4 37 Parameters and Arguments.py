def greet(name: str, language: str, default: str):
     if language == 'it':
         print(f'Ciao {name}')

     else:
         print(f'{default}, {name}!')


greet(name='Mario' , language='it', default = 'Hello')

