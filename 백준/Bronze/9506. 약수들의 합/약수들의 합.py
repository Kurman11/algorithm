while 1:
    num = int(input())

    if num == -1:
        break
    a = []
    for i in range(1,num):
        if num % i == 0:
            a.append(i)
        
    if sum(a)== num :
        print(num,' = ',' + '.join(str(i) for i in a),sep='')
    else:
        print(num,'is NOT perfect.')