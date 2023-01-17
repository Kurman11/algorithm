cnt = 0
X = []
Y = []

for i in range(3):
    x, y =list(map(int,input().split()))
    X.append(x)
    Y.append(y)

for t in range(3):
    if X.count(X[t]) == 1:
        num1 = X[t]
    elif Y.count(Y[t]) == 1:
        num2 = Y[t]

print(num1,num2)