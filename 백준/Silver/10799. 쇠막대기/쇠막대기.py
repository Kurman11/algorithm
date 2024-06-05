n = list(input())
b = 0
c = 0
st = []

for i in range(len(n)):
    if n[i] == '(' :
        b += 1
    else:
        b -= 1
        if n[i-1] == '(':
            c += b
        else:
            c += 1

print(c)