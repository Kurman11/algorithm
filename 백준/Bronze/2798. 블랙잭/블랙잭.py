num1 = list(map(int,input().split()))
num2 = list(map(int,input().split()))
a = []

for i in range(num1[0]-2):
    for x in range(i+1, num1[0]-1):
        for t in range(x+1, num1[0]):
            if num2[i]+num2[x]+num2[t] <= num1[1]:
                a.append(num2[i]+num2[x]+num2[t])
print(max(a))