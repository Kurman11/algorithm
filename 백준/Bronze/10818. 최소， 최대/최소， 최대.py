T = int(input())
num_list = list(map(int,input().split()))
a = sorted(num_list)
print(a[0],a[-1])