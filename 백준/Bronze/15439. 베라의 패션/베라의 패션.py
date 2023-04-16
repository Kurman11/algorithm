N = int(input())
cnt =0
for i in range(N):
    for j in range(N):
        if i !=j :
            cnt += 1

print(cnt)