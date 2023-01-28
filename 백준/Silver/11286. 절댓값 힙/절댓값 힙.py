import heapq, sys
heap = []
N = int(input())

for n in range(N):
    x = int(sys.stdin.readline())
    
    if x == 0:
        if heap:    # 비어있지 않으면
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    
    else:
        heapq.heappush(heap, (abs(x),x))