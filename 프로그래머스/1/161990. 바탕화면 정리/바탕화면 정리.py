def solution(wallpaper):
    c, r = [], [] #열,행 리스트
    for i in range(len(wallpaper)):#열
        for j in range(len(wallpaper[i])): #행
            if wallpaper[i][j] == "#": # #인경우
                c.append(i) #열 리스트에 추가
                r.append(j) #행 리스트에 추가
    #열 리스트 중에 가장 작은 값, 행 리스트 중에 가장 작은 값, 열 리스트 중에 가장 큰 값, 행 리스트 중에 가장 큰 값
    return [min(c), min(r), max(c) + 1, max(r) + 1]