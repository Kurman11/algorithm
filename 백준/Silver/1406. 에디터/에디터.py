left = list(input())
right = []
n = int(input())

for i in range(n):
    arr = list(input().split())
    if arr[0] == 'L' and left:
        right.append(left.pop())
    elif arr[0] == 'D' and right:
        left.append(right.pop())
    elif arr[0] == 'B' and left:
        left.pop()
    elif arr[0] == 'P':
        left.append(arr[1])

ans = left + right[::-1]
print("".join(ans))