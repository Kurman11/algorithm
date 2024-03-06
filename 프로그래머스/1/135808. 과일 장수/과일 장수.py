def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    


    for i in range(0, len(score), m):
        temp = score[i:i+m]
        
        if len(temp) == m:
            answer += (min(temp) * m)
    return answer

def test_sample():
    assert solution(3, 4, [1, 2, 3, 1, 2, 3, 1]) == 8
    assert solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 1, 4, 2]) == 33