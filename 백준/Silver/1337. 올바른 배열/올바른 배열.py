import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

data.sort()

maxVal = 0
for i in range(n):
    cnt = 0
    res = []
    for j in range(data[i]+1,data[i]+5):
        res.append(j)
    
    for d in data:
        if d in res:
            cnt += 1
    
    if cnt > maxVal:
        maxVal = cnt
print(4-maxVal)