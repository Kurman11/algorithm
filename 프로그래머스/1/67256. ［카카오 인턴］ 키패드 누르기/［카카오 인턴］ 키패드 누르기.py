from collections import deque

loc = {  # 키패드
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2),
    '*': (3, 0), 0: (3, 1), '#': (3, 2)
}


def bfs(dest, thumb):  # 최단거리
    q = deque()
    q.append(loc[dest])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    visited = [[0] * 3 for _ in range(4)]
    x, y = loc[dest]
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 4 and 0 <= ny < 3:
                if visited[nx][ny] == 0:  # 방문 X
                    if (nx, ny) == thumb:
                        return visited[x][y]

                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

    return 0


def left_or_right(dest, left, right, hand):  # 어떤 엄지로 누를것인가?
    lm = bfs(dest, left)
    rm = bfs(dest, right)

    if lm < rm:
        return 'L'
    elif rm < lm:
        return 'R'
    else:
        if hand == "left":
            return 'L'
        else:
            return 'R'


def solution(numbers, hand):
    answer = ''

    left, right = (3, 0), (3, 2)
    for i in numbers:
        if i in (1, 4, 7):
            answer += 'L'
            left = loc[i]
        elif i in (3, 6, 9):
            answer += 'R'
            right = loc[i]
        else:
            answer += left_or_right(i, left, right, hand)
            if answer[-1] == 'L':
                left = loc[i]
            else:
                right = loc[i]

    return answer