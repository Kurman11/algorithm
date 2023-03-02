def solve(n: int) -> str:
    return 'long ' * (n // 4) + 'int'

if __name__ == '__main__':
    n = int(input())

    print(solve(n))