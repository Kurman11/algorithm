from itertools import combinations

def solution(nums):
    answer = 0
    
    # 조합 리스트 만들기
    comb_list = list(combinations(nums, 3))
    comb_sum_list = [sum(n) for n in comb_list]
    
    n = max(comb_sum_list)
    prime_nums = set(range(2, n + 1))
    
    # sum 중에 가장 큰 값까지 소수 리스트 구하기
    for i in range(2, n + 1):
        if i in prime_nums:
            prime_nums -= set(range(2 * i, n + 1, i))
            
    # sum 리스트 중 소수 몇 개인지 확인하기
    for n in comb_sum_list:
        if n in prime_nums:
            answer += 1
    
    return answer