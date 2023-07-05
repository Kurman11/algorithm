word = input()

num = len(word)
result = []

for i in range(num):
    for x in range(i, num):
        result.append(''.join(word[x - i:x + 1]))
result = set(result)

print(len(result))