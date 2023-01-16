T = int(input())
a = []

for t in range(1,T+1):
    num = int(input())
    a.append(num)
b = a.count(0)
c = a.count(1)

if b > c:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")