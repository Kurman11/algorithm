
def solution(n, m):
    answer = []
    # 최대 공약수
    value = min(n, m)
    for i in range(value, 0, -1) :
        if n % i == 0 and m % i == 0 :
            answer.append(i)
            break
    # 최소 공배수
    value = max(n, m)
    for i in range(value, value * value) :
        if i % n == 0 and i % m == 0 :
            answer.append(i)
            break
            
    return answer