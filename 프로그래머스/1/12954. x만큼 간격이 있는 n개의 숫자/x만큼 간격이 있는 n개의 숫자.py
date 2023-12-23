def solution(x, n):
    result = [] # result 리스트 선언
    a = x   # 변수 a에 값 x을 저장합니다.
    
    for i in range(n):  # n값의 개 수 만큼 반복합니다.
        result.append(x)    # result 리스트에 현재에 해당하는 x값을 추가합니다.
        x += a  # x = x + a입니다. 즉, 현재 값 x에 a를 더해줍니다.
    
    return result