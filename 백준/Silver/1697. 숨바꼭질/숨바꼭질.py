def bfs(s,e):
    q = []
    v = [0] * 200001

    q.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)
        if c == e:
            return v[e] - 1
        
        for i in ((c-1), (c+1), (c*2)):
            if 0 <= i < 200000 and v[i] == 0:
                q.append(i)
                v[i] = v[c] + 1

N,K = map(int,input().split())
ans = bfs(N,K)
print(ans)
