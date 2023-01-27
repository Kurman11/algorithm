import heapq

num = list(map(int,input().split()))

heapq.heapify(num)
heapq.heappop(num)
print(num[0])

