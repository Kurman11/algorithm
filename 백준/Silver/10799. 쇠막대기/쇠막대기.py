T = list(input())
count = 0  
open_count = 0  

for i in range(len(T)):
    if T[i] == '(':
        open_count += 1
    else:
        open_count -= 1
        if T[i-1] == '(':  
            count += open_count
        else:
            count += 1

print(count)