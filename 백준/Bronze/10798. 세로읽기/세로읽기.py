a = [input()for _ in range(5)]


for t in range(15):   
    for x in range(5):
        try:
            print(a[x][t], end = '')
        except:
            continue