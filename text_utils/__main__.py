from .sort import sort
from .unique import unique


def main():
    print(sort(["aaaa", "aba", "bbb", "aaa", "bab"]))
    print(unique(["123", "345", "123", "654", "345"]))


if __name__ == '__main__':
    main()

