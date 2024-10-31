T = int(input())

for i in range(1, T+1):
    num_str = str(i)
    clap_count = num_str.count('3') + num_str.count('6') + num_str.count('9')
    
    if clap_count > 0:
        print('-' * clap_count, end=' ')
    else:
        print(i, end=' ')