def description(numbers: list[int]) -> dict:
    details: dict = {'length': (n_length := len(numbers)),
                     'sum': (n_sum := sum(numbers)),
                     'mean': n_sum / n_length}

    return details

def main() -> None:
    print(x := 1 > 0)
    print(x)

if __name__ == '__main__':
    main()

