T = int(input())
table = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")

for i in range(1, T+1):
    s = input()
    d = ''
    for j in range(len(s)):
        num = table.index(s[j])
        bin_num = str(bin(num)[2:])
        while len(bin_num) < 6:
            bin_num = '0' + bin_num
        
        d += bin_num
    r = ''
    for w in range(len(s)*6//8):
        e = int(d[w*8:w*8+8],2)
        r += chr(e)
    
    print(f'#{i} {r}')