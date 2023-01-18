cnt = 0
result = input()
for i in range(len(result)):
    if result[i] == '@':
        cnt += 1
    elif result[i] == '(':
        break
result1 = result[::-1]
cnt1 = 0
for x in range(len(result)):
    if result1[x] == '@':
        cnt1 +=1
    elif result[-x] == ')':
        break

print(cnt,cnt1)