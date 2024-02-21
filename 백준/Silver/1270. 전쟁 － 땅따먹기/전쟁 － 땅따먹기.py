n = int(input())
 
for _ in range(n):
    d = dict()
    line = input().split()
    t = int(line[0])
    max_val = 0
    max_key = 0 
    for i in range(1, len(line)):
        num = int(line[i])
        if num not in d:
            d[num] = 1
        else:
            d[num] += 1
        if d[num] > max_val:
            max_val = d[num]
            max_key = num
    if max_val > t / 2:
        # 전쟁 끝
        print(max_key)
    else:
        print('SYJKGW')