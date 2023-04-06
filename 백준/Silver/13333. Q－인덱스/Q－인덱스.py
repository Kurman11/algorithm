T = int(input())
num = sorted(list(map(int,input().split())))

for i in range(T, -1 , -1):
    if i <= num[-i]:
        print(i)
        break