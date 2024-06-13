E, S, M = map(int, input().split())

cnt = 1
Earth, Sun, Moon = 1, 1, 1

while (Earth, Sun, Moon) != (E, S, M):
    Earth = (Earth % 15) + 1
    Sun = (Sun % 28) + 1
    Moon = (Moon % 19) + 1
    cnt += 1

print(cnt)