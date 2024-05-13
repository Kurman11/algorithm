numbers = [0, 1, 2, 4, 11, 12, 14, 21, 22, 24, 41, 42, 44]


def solution(n):
    answer = recursion(n)
    return str(answer)


def recursion(q):
    mod = [1, 2, 4]
    if q >= len(numbers):
        tmp = recursion((q - 1) // 3) * 10 + mod[(q - 1) % 3]
        return tmp
    else:
        return numbers[(q-1)//3] * 10 + mod[(q - 1) % 3]