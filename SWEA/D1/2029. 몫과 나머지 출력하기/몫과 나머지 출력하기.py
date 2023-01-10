T = int(input())
for t in range(1,T+1):
    a,b = list(map(int,input().split()))
    y = a//b
    u = a % b
    print(f"#{t} {y} {u}")