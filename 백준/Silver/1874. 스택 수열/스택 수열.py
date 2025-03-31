n = int(input())
st = []
rst = []
crt = 1
temp = True

for i in range(1, n+1):
    num = int(input())
    while crt <= num:
        st.append(crt)
        rst.append('+')
        crt += 1
    
    if st[-1] == num:
        st.pop()
        rst.append('-')
    else:
        temp = False
        break

if temp == False:
    print('NO')
else:
    for i in rst:
        print(i)