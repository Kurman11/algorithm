def solution(arr, divisor):
    answer = [num for num in arr if num % divisor == 0]
    return sorted(answer) or [-1]