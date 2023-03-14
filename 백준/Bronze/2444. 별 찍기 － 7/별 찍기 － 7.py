n = int(input())
for i in range(1, n):
    print(' '*(n-i) + '*'*(2*i-1))

for x in range(n, 0, -1):
    print(' '*(n-x) + '*'*(2*x-1))