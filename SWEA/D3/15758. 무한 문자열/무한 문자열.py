import math

T = int(input())

for i in range(1 , T+1):
    S, T = map(str,input().split())
    num_1,num_2  = len(S), len(T)
    
    lcm = (num_1 * num_2) // math.gcd(num_1, num_2)

    a = S * (lcm//num_1)
    b = T * (lcm//num_2)

    if a == b:
        print(f"#{i} yes")
    else:
        print(f"#{i} no")