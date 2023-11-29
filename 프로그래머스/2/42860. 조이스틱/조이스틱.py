def solution(name):
    answer = 0
    name = list(name)
    min_move = len(name) - 1
    for i in range(len(name)):
        answer += min(ord(name[i]) - ord('A') , ord('Z') - ord(name[i]) + 1)
        next_d = i + 1
        up_d = 0
        while next_d < len(name) and name[next_d] == 'A':
            next_d += 1
        min_move = min(min_move, i + i + len(name) - next_d)
        min_move = min(min_move, (len(name)-next_d) * 2 + i)
    
    answer += min_move
        
    return answer