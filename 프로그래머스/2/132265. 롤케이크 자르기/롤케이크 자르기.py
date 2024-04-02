from collections import Counter 

def solution(topping):
    answer = 0
    old = Counter(topping) # 처음에 전부 형꺼 
    young = set()  #동생꺼 
        
    for i in topping:
        old[i] -= 1
        young.add(i) #토핑을 하나씩 동생이 가지고 감 
        
        if old[i] == 0:
            old.pop(i) #키를 빼는 것은 형이 더이상 해당 토핑을 가지고 있지 않음을 뜻함
        if len(old) == len(young): #두 형제의 토핑 갯수가 같다면 1로 세림
            answer += 1 
            
    return answer