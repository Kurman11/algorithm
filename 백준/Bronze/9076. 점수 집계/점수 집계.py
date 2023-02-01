T = int(input())

for t in range(1,T+1):
    num = list(map(int,input().split()))
    num.remove(max(num)) 
    num.remove(min(num))
    # num = sorted(num)
    if (max(num) - min(num)) < 4:
        print(sum(num))
    else:
        print('KIN')