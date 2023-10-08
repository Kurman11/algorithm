N = int(input())
true_value = [0] * 51
true_flag = []
num = list(map(int,input().split()))
for i in range(N):
    true_value[num[i]] = true_value[num[i]] + 1
for j in range(len(true_value)):
    if j == true_value[j]:
        true_flag.append(j)
if true_flag == []:
    print(-1)
else: print(max(true_flag))