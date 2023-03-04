import sys
N,K = map(int,input().split())
A = list(map(int,input().split()))
cnt = 0
answer = []

def heap_sort(a,n):
    global cnt
    build_min_heap(a,n)
    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        cnt += 1
        if cnt == K:
            answer.extend([a[0], a[i]])
        heapify(a, 0, i)


def build_min_heap(a,n):
    for i in range((n//2), -1, -1):
        heapify(a, i, n)

def heapify(a, k, n):
    global cnt
    l = 2 * k + 1
    r = 2 * k + 2
    if l < n and a[l] < a[k]:
        smaller = l
    else:
        smaller = k
    if r < n and a[r] < a[smaller] :
        smaller = r
    if smaller != k:
        a[k], a[smaller] = a[smaller], a[k]
        cnt += 1
        if cnt == K:
            answer.extend([a[k], a[smaller]])
        heapify(a, smaller, n)

heap_sort(A,N)
if not answer:
    print('-1')
else:
    print(*sorted(answer))