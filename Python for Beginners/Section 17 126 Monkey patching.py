import time
import logging

class Internet:
    def __init__(self, provider: str) -> None:
        self.provider = provider

    def connect(self) -> None:
        print(f'[{self.provider}] Connecting...')
        time.sleep(2)
        print(f'[{self.provider}] You are now connected!')

def test_connect() -> None:
    print('[Provider] You are connected!')

def main() -> None:
    internet: Internet = Internet('Verizon')

    internet.connect = test_connect #type: ignore
    internet.connect()

if __name__ == '__main__':
    main()