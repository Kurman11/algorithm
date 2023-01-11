num = int(input())

a = 0
while num> 0:
    a += num%10
    num //= 10
    
print(a)
    