num = int(input())
cnt =0
num_str = str(num)

if len(num_str) == 1:
    num_str = '0' + num_str

while 1:
    result = 0
    for i in str(num_str):
        result +=int(i)
    for t in str(result):
        pass
    num_str = int(i + t)

    cnt += 1

    if num == num_str:
        break

print(cnt)
