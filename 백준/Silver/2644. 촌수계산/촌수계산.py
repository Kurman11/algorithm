from collections import deque

def bfs(s,e):
    q = deque()
    q.append(s)
    v = [0] * (T+1)
    v[s] = 1

    while q:
        c = q.popleft()
        if c == e:
            return v[e] - 1

        for n in arr[c]:
            if not v[n]:
                q.append(n)
                v[n] += v[c] + 1
    return -1

T = int(input())
n,p = map(int,input().split())
num = int(input())
arr = [[] for _ in  range(T+1)]

for i in range(num):
    a,c = map(int,input().split())
    arr[a].append(c)
    arr[c].append(a)

ans = bfs(n,p)
print(ans)