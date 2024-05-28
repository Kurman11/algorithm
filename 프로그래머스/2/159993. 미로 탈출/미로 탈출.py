from collections import deque

def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    
    graph = [list(maps[i]) for i in range(n)]
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'S':
                start_y, start_x = i, j 
            elif graph[i][j] == 'E':
                end_y, end_x = i, j 
            elif graph[i][j] == 'L':
                lever_y, lever_x = i, j 
            

    dy= [1,0,-1,0]
    dx= [0,-1,0,1]
    def bfs(start_y, start_x, end_y, end_x):
        chk[start_y][start_x] = 0
        q= deque()
        q.append((start_y, start_x))

        while q:
            y,x = q.popleft()
            if y == end_y and x == end_x:
                return chk[y][x]
            
            for k in range(4):
                ny = y+ dy[k]
                nx = x+ dx[k]
                if 0<=ny<n and 0<=nx<m:
                    if graph[ny][nx] != 'X' and chk[ny][nx] =='inf':
                        chk[ny][nx] = chk[y][x] + 1
                        q.append((ny,nx))
        return None 
    
    
   
    # 출발지에서 lever까지 거리 구하기 
    chk = [['inf'] * m for _ in range(n)]
    distance1 = bfs(start_y, start_x, lever_y, lever_x)
    
   # lever에서 도착지까지 거리 구하기
    chk = [['inf'] * m for _ in range(n)]
    distance2 = bfs(lever_y, lever_x, end_y,end_x)
    
    if distance1 is None or distance2 is None:
        return -1
    else:
        return distance1+distance2