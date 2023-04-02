num = int(input())
cnt = 1
cnt1 = 0
 
for i in range(num):
    cnt += 6 * i
    cnt1 += 1
    if cnt >= num:
        break

print(cnt1)