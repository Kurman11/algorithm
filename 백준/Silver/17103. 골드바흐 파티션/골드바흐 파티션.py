import sys

prime = []
ck = [0] * 1000001
ck[0] = 1
ck[1] = 1

for i in range(2, 1000001):
    if ck[i] == 0:
        prime.append(i)
        for j in range(2*i, 1000001, i):
            ck[j] = 1

T = int(sys.stdin.readline())

for _ in range(T):
    cnt = 0
    N = int(sys.stdin.readline())
    for i in prime:
        if i >= N:
            break
        if not ck[N - i] and i <= N-i:
            cnt += 1
    print(cnt)