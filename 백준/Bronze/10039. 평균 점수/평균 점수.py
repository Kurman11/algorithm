num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

num = [num1,num2,num3,num4,num5]
num_list = []
for i in num:
    if i < 40:
        i = 40
        num_list.append(i)
    else:
        num_list.append(i)

a = int(sum(num_list)/5)

print(a)