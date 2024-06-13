E, S, M = map(int,input().split())

cnt = 1
Earth = 1
Sun = 1
Moon = 1

while 1:
    if (Earth, Sun, Moon) ==  (E, S, M):
        break

    if 1 <= Earth <= 15 and 1 <= Sun <= 28 and 1 <= Moon <= 19:
        Earth += 1
        Sun += 1
        Moon += 1
        cnt += 1

    elif Earth > 15:
        Earth = 1
        
    elif Sun > 28:
        Sun = 1

    elif Moon > 19:
        Moon = 1
    
print(cnt)