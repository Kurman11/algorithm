lst = [list(map(int,input().split())) for _ in range(9)]
a = []

for _ in range(9):
    a.append((max(lst[_])))

for i in range(9):
    for x in range(9):
        if max(a) == lst[i][x]:
            print(max(a))
            print(i+1,x+1)