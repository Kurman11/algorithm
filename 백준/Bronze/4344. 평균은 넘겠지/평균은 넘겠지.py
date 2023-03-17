T = int(input())

for t in range(T):
    num = list(map(int,input().split()))
    for i in range(num[0]):
        cnt = 0
        average = sum(num[1:])/num[0]
        for x in num[1:]:
            if average < x:
                cnt += 1
            a = (cnt / num[0])*100


    print(f'{a:.3f}%')