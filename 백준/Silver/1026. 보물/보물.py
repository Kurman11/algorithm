T = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
B = B[::-1]
num = 0
for i in range(T):
    num += A[i] * B[i]

print(num)