a = []
b = []
num = [int(input()) for _ in range(10)]
num1 = [int(input()) for _ in range(10)]

a = sorted(num)
b = sorted(num1)

print(sum(a[-3::]), sum(b[-3::]))