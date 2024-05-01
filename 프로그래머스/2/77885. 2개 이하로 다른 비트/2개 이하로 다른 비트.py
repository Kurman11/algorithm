def solution(numbers) :
    answer = []
    for number in numbers :
        bin_num = list('0' + bin(number)[2:])
        index = ''.join(bin_num).rfind('0')
        bin_num[index] = '1'

        if number % 2 == 1 :
            bin_num[index+1] = '0'

        answer.append(int(''.join(bin_num), 2))

    return answer