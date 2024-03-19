d = {i:str(i) for i in range(0, 10)}
d[10] = 'A'
d[11] = 'B'
d[12] = 'C'
d[13] = 'D'
d[14] = 'E'
d[15] = 'F'

def nary(x, n):
    if x == 0:
        return '0'
    
    res = []
    
    while x > 0:
        x, mod = divmod(x, n)
        res.append(d[mod])
    
    return ''.join(res)[::-1]
    
def solution(n, t, m, p):
    s = ''.join(nary(i, n) for i in range(30000))
    
    # (p-1) + m*i 번째 인덱스만 추출
    return ''.join(s[(p-1) + m * i] for i in range(t))