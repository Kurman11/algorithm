def hanoi(num, one, two, three):
    if num == 1:
        print(one, two)
    else:
        hanoi(num-1, one, three, two)
        print(one, two)
        hanoi(num-1, three, two, one)



num = int(input())
print((2 ** num) -1)
hanoi(num, 1,3,2)