N, M = map(int,input().split())
dik = dict()

for i in range(N):
    word = input()
    if word in dik:
        if len(word) < M:
            pass
        else:
            dik[word] += 1
    else:
        if len(word) < M:
            pass
        else:
            dik[word] = 1

sorted_items = sorted(dik.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

# Printing the sorted items
for key, value in sorted_items:
    print(key)