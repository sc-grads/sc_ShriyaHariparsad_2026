import time
from functools import cached_property

class DataSet:
    def __init__(self, data: list[float]) -> None:
        self._data = data
    def show_data(self) -> None:
        print(self._data)



    @cached_property

    def sum(self) -> float:
        print('Calculating sum...')
        time.sleep(2)
        return sum(self._data)

    @cached_property
    def mean(self) -> float:
        print('Calculating mean...')
        time.sleep(2)
        return sum(self._data) / len(self._data)

def main() -> None:
    ds: DataSet = DataSet([1.5, 2.5, 10, 7])
    ds.show_data()

    while True:
       user_input: str = input('You: ').lower()

       if user_input == 'clear sum':
           del ds.sum
           print('Sum cache cleared!')
       elif user_input == 'clear mean':
           del ds.mean
           print('Mean cache cleared!')
       elif user_input == 'sum':
           print(ds.sum)
       elif user_input == 'mean':
           print(ds.mean)
       else:
           print('Unknown command...')


if __name__ == '__main__':
    main()

