from itertools import permutations
n = int(input())
lst = list(map(int, input().split()))

max_result = 0

# 모든 가능한 순열을 검사
for perm in permutations(lst):
    result = 0
    for i in range(n-1):
        result += abs(perm[i] - perm[i + 1])
    if result > max_result:
        max_result = result

print(max_result)