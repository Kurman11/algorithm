def spin_list(rst):                 # 리스트 회전시키기
    tup = zip(*rst[::-1])           # zip으로 회전시킬 경우, tuple형태로 묶이기 때문에
    return [list(x) for x in tup]   # return하면서 list로 바꾸는 과정이 필요

def solution(m, n, board):          # m : x축, n : y축. 여기서는 회전시키므로 바꿔서 사용
    field = spin_list(board)
    answer = 0
    while True:
        flag = False
        visited = [[0]*m for _ in range(n)]     # 같은 블록이 여러 2x2에 포함될 수 있으므로 바로 변환하면 안됨 -> 변환할 좌표 리스트
        for i in range(n-1):
            for j in range(m-1):
                if field[i+1][j+1] != 0 and field[i][j] == field[i+1][j] == field[i][j+1] == field[i+1][j+1]:
                    # 4개가 같은 지 확인. 이것도 for문처리하고 싶었지만, 그러려면 for문이 4개가 더 필요해서 수작업
                    visited[i][j] = 1
                    visited[i+1][j] = 1
                    visited[i][j+1] = 1
                    visited[i+1][j+1] = 1
                    flag = True
        
        if not flag:                # 바뀐 게 없다면 : 아래의 과정이 필요가 없으니까 종료
            break
        
        for i in range(n):
            for j in range(m):
                if visited[i][j]:       # 바뀌었다면
                    field[i][j] = -1    # -1로 (일단) 바꿔주고
                    field[i].append(0)  # 뒤에 0을 집어넣음(리스트의 전체 길이 유지)
                    answer += 1

            field[i] = [x for x in field[i] if x != -1] # -1을 없애기
        

    return answer