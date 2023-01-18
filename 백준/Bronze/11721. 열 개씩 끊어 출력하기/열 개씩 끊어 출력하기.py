str1 = input()
cnt = 0
for i in str1:
    cnt += 1
for x in range(0,cnt,10):
    print(str1[x:x+10])