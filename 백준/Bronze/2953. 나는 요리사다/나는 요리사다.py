num_list =[]
cnt = 0
for i in range(5):
    num = list(map(int,input().split()))
    num_list.append(sum(num))

print(num_list.index(max(num_list))+1,max(num_list))