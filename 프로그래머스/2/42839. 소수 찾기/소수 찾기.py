from itertools import permutations

def solution(numbers):
    answer = 0
    
    
    # 1. 숫자 따로 떼주기
    arr = []
    
    for num in numbers:
        for n in num:
            arr.append(n)
            
    
    # 2. 순열 집합 만들기
    nPr = set()
    
    for i in range(1, len(arr) + 1):
        temp = list(permutations(arr, i))
        for n in temp:
            nPr.add(int(''.join(n)))
            
    
    # 3. 소수인지 판별하기
    n = max(nPr)
    primeNums = set(range(2, n + 1))
    
    for i in range(2, n + 1):
        if i in primeNums:
            primeNums -= set(range(2 * i, n + 1, i))
    
    for t in nPr:
        if t in primeNums:
            answer += 1
            
    return answer