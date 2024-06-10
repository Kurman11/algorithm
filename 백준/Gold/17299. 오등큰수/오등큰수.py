from collections import Counter

n = int(input())
lst = list(map(int,input().split()))
st = []

freq = Counter(lst)

# 결과를 저장할 리스트를 -1로 초기화
result = [-1] * n
stack = []

# 왼쪽에서 오른쪽으로 탐색
for i in range(n):
    # 스택의 탑에 있는 원소의 오등큰수가 될 때까지 pop
    while stack and freq[lst[stack[-1]]] < freq[lst[i]]:
        result[stack.pop()] = lst[i]
    # 현재 인덱스를 스택에 push
    stack.append(i)

print(*result)