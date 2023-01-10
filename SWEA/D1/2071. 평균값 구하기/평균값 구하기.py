T = int(input())

for t in range(1,T+1):
    numbers = list(map(int,input().split()))
    x = sum(numbers)/len(numbers)
    average = round(x,0)

    print(f"#{t} {int(average)}")