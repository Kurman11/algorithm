def solution(n, lost, reserve):
    answer = 0
    # 정렬 
    lost.sort()
    reserve.sort()
    # 여벌있으면서 도난 당한 경우 
    for r in reserve[:]:
        if r in lost:
            reserve.remove(r)
            lost.remove(r)
    # 여벌이 있는 경우 빌려주고 lost 배열에서 제거         
    for r in reserve[:]:
        if r-1 in lost:
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)
            
    return n-len(lost)