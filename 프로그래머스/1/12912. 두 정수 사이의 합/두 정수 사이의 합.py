def solution(a, b):
    if a>b:
        a,b=b,a
    my_list=list(range(a,b+1))
    answer = sum(my_list)
    return answer