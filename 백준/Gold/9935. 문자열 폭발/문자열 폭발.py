word1 = str(input())
word2 = str(input())
stack = []
word2_len = len(word2)

for char in word1:
    stack.append(char)
    if len(stack) >= word2_len and ''.join(stack[-word2_len:]) == word2:
        del stack[-word2_len:]  # stack에서 word2 제거

result = ''.join(stack)
if result:
    print(result)
else:
    print('FRULA')