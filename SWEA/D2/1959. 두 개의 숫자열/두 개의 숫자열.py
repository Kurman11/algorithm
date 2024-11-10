T = int(input())

for i in range(1, T+1):
    N, M = map(int,input().split())
    Ai = list(map(int,input().split()))
    Bi = list(map(int,input().split()))
    if len(Ai) < len(Bi):
        rst = 0
        while len(Ai) <= len(Bi):
            n = 0
            for j in range(len(Ai)):
                n += Ai[j] * Bi[j]
            rst = max(n, rst)
            Bi.pop(0)
    
    else:
        rst = 0
        while len(Ai) >= len(Bi):
            n = 0
            for j in range(len(Bi)):
                n += Ai[j] * Bi[j]
            rst = max(n, rst)
            Ai.pop(0)
    
    print(f'#{i} {rst}')