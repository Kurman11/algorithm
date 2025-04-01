n,m = list(map(int, input().split()))
arr = []
rst = []
cnt = 0

for i in range(1, n+1):
    arr.append(i)

for i in range(n):
    cnt += m -1
    if cnt >= len(arr):
        cnt = cnt % len(arr)
    rst.append(str(arr.pop(cnt)))

print('<',", ".join(rst),">",sep='')