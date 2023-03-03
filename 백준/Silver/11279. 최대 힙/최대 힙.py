import sys,heapq

T = int(sys.stdin.readline())
a = []
b = []
for i in range(T):
    num = int(sys.stdin.readline())

    if num == 0:
        if a:
            print(heapq.heappop(a)[1])
        else:
            print(0)
    else:
        heapq.heappush(a,[-num, num])