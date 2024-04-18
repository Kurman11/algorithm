def solution(board, h, w):
    length = len(board[0])

    numberOfSameColor = 0

    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]

    for i in range(4):
        h_check, w_check = h + dh[i], w + dw[i]

        if 0 <= h_check < length and 0 <= w_check < length:
            if board[h_check][w_check] == board[h][w]:
                numberOfSameColor += 1

    return numberOfSameColor