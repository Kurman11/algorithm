def solution(x):
    arr = list(str(x))  # arr 변수에 x값을 string값으로 변환한 후 리스트화
    a = 0   # 변수 a 선언
    
    for i in arr:   # 리스트 arr의 개 수 만큼 반복
        a += int(i) # string값인 i를 int화 한다음 a에 +
    
    if x % a == 0:  # x / a 의 나머지가 0이면 true
        result = (x % a == 0)   # x % a == 0이 true이니깐 true 반환
    else:
        result = (x % a == 0)   # x % a == 0이 false이니 false 반환
    return result
 