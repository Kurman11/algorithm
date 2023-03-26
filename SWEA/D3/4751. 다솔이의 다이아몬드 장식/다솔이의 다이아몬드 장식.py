T = int(input())

for t in range(1,T+1):
    word = input()
    n = len(word) 

    if n == 1:
        print('..#..''\n''.#.#.''\n'f'#.{word}.#''\n''.#.#.''\n''..#..')
    elif n >= 2:
        for i in range(n):
            print("..#.", end="")
            if i == n-1:
                print(".")

        for i in range(n):
            print('.#.#',end='')
            if i == n-1:
                print('.')
        
        for i in range(n):
            print('#.'f'{word[i]}.',end='')
            if i == n-1:
                print('#')
        
        for i in range(n):
            print('.#.#',end='')
            if i == n-1:
                print('.')

        for i in range(n):
            print("..#.", end="")
            if i == n-1:
                print(".")