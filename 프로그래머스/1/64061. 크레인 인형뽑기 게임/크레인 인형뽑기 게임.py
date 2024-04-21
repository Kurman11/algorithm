def solution(board, moves):
    # (1) board를 n개의 column vector로 변환해야함.
    n = len(board) # board의 column 수
    column_board = [[0]*n for _ in range(n)]
    for i in range(n):
        board_i = board[i] # i번째 행
        for j in range(n):
            column_board[j][i] = board_i[j] # transpose
    
    # (2) moves의 move에 맞는 column vector에서 하나씩 추출
    basket = [] # 바구니
    cnt = 0 # 터뜨린 인형 count
    for move in moves:
        move = move-1 # column 지정 : 1번 move -> 0번 column
        target = column_board[move]
        i = 0
        while True:
            if i == n:
                # 해당 리스트 텅텅 빔 (0으로만 이루어진 list)
                break
            # 0이 아닌 원소가 나오면 break하고 basket으로 옮김
            if target[i] != 0:
                a = target[i] # 집은 인형
                column_board[move][i] = 0 # 해당 위치의 인형을 집었으므로 0으로 초기화
                if len(basket) == 0:
                    basket.append(a)
                    break
                else:
                    if basket[-1] == a: # 집은 인형이 basket의 마지막에 있던 거랑 같다면
                        basket.pop()
                        cnt += 2
                    else:
                        basket.append(a)
                    break
            else:
                i += 1
            
    answer = cnt
    return answer