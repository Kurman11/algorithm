import sys
num = list(sys.stdin.readline().strip())
num1 = num[:]
cnt0 = 0
cnt1 = 0

while 1:
    if num[0] == '1':
        num.append(num.pop(0))
    else:
        i = 1
        while 1:
            if num[0] == num[i]:
                num[i] = '1'
                i += 1
                if i == len(num):
                    break
            else:
                cnt1 += 1
                break
        num[0] = '1'
        num.append(num.pop(0))
    if len(num) == num.count('1'):
        break

while 1:
    if num1[0] == '0':
        num1.append(num1.pop(0))
    else:
        x = 1
        while 1:
            if num1[0] == num1[x]:
                num1[x] = '0'
                x += 1
                if x == len(num1):
                    break
            else:
                cnt0 += 1
                break
        num1[0] = '0'
        num1.append(num1.pop(0))
    if len(num1) == num1.count('0'): 
        break

print(min(cnt0,cnt1))