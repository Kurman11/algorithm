T = int(input())

for i in range(1, T+1):
    s = list(input())
    b = s[::-1]
    for j in range(len(s)):
        if b[j] == s[j]:
            pass
        else:
            print(f'#{i} 0')
            break
        
        if j == len(s)-1:
            print(f'#{i} 1')