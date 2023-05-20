N, K = map(int,input().split())
num = list(map(int,input().split()))
num = sorted(num)
print(num[-K:][0])