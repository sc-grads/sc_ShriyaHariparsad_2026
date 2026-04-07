class Connection:
    def __init__(self, connection_type: str) -> None:
        self.connection_type = connection_type

    def connect(self) -> None:
        print(f'Connecting to: {self.connection_type}')

def connect(connection_type: str) -> None:
        print(f'Connecting to: {connection_type}')