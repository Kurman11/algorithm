T = int(input())
a = 0
b = 0
for t in range(1,T+1):
    num = int(input())
    num_list = list(map(int,input().split()))
    for i in range(num):
        if num_list[i] <= 10:
            a = sum(num_list)
    print(a)