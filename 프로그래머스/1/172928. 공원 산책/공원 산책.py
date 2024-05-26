def solution(park, routes):
    # 방향 정의(x,y)
    move_dic = {'E':[0,1],'W':[0,-1],'S':[1,0],'N':[-1,0]}
    H,W = len(park)-1,len(park[0])-1

    # 출발위치 찾기
    robot = [0,0]
    for i,x in enumerate(park):
        if 'S' not in x: continue   # 해당 행에 S가 없는 경우 skip
        for j,y in enumerate(x):
            if 'S'==y:
                robot=[i,j]         # 초기화
                park[i]= park[i].replace('S','O')   # 이동가능으로 변경
                break
                
    # 시뮬레이션 시작
    for route in routes:
        cur = robot                 # 명령 시작 위치 저장
        direction, walks = route.split(" ")
        for _ in range(int(walks)):
            # 다음 스텝
            x,y = cur[0]+move_dic[direction][0],cur[1]+move_dic[direction][1]
            # 이동이 어려운 경우 해당 명령 시행 전으로 초기화
            if (x>H or x<0 or y>W or y<0) or ('X' == park[x][y]):
                cur = robot
                break
            else:
                cur=[x,y]
        robot=cur
        
    return robot