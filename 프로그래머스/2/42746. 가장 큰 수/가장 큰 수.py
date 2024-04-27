from functools import cmp_to_key

def solution(numbers):
    answer = ''
    
    def compare(a, b):
        a = str(a)
        b = str(b)
        
        # 그리디 개념 적용
        s1 = int(a + b)
        s2 = int(b + a)
        
        if s1 < s2:
            return 1
        elif s1 > s2:
            return -1
        else:
            return 0
    
    numbers.sort(key=cmp_to_key(compare))
    
    # 00, 000 같은 경우를 고려한 형변환
    answer = str(int("".join(map(str, numbers))))
    
    return answer