T = int(input())

for t in range(1,T+1):
    Quarter = 0
    Dime = 0
    Nickel = 0
    Penny = 0

    num = int(input())
    
    Quarter += num // 25
    num = num % 25

    Dime += num //10
    num = num % 10

    Nickel = num // 5
    num = num % 5

    Penny = num // 1

    print(Quarter,Dime,Nickel,Penny)