T = int(input())
cnt = 0
lst = []

for _ in range(T):
    name = input()
    K,M = list(map(int,input().split()))
    num = 0
    while K <= M:
        M -= K
        M += 2
        num += 1
    
    cnt += num
    lst.append((name,num))

max_pokemon = max(lst, key=lambda x: x[1])
print(cnt)
print(max_pokemon[0])