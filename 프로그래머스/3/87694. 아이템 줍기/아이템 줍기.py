from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    arr = [[0] * 101 for _ in range(101)]
    cx = characterX * 2
    cy = characterY * 2
    ix = itemX * 2
    iy = itemY * 2
    visited = [[0] * 101 for _ in range(101)]
    visited[cx][cy] = 1
    q = deque()
    q.append((cx,cy))
    
    for i in rectangle:
        a,b,c,d = i
        for row in range(2*a, 2*c+1):
            for col in range(2*b, 2*d+1):
                arr[row][col] = 1
                
    for i in rectangle:
        a,b,c,d = i
        for row in range(2*a+1, 2*c):
            for col in range(2*b+1, 2*d):
                arr[row][col] = 0
    
    while q:
        x,y = q.popleft()
        if (x,y) == (ix,iy):
            answer = arr[x][y] // 2
            break
        for i,j in ((1,0), (0,1), (-1,0), (0,-1)):
            dx , dy = i+x , y+j
            if 0 <= dx < 101 and 0 <= dy < 101 and arr[dx][dy] != 0 and visited[dx][dy] == 0:
                arr[dx][dy] = arr[x][y] + 1
                visited[dx][dy] = 1
                q.append((dx,dy))
    return answer