n = int(input())

for i in range(n):
    word = input().split()
    for j in word:
        print(j[::-1], end=' ')