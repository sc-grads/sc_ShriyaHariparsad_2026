status: int = 200

match status:
    case 200:
        print('Connected!')
    case 403:
        print('Forbidden...')
    case 404:
        print('Not Found...')
    case _:
        print('Unknown...')