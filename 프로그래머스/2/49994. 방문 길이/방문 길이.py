def solution(dirs):
    # 가본 길을 (x1, y1, x2, y2) 형태로 저장해둔 set을 관리하면 됩니다.
    # 단, 출발점과 도착점 구분이 없으므로,
    # (x2, y2, x1, y1)도 함께 저장해둔 뒤에 마지막에 개수를 2로 나눕니다.
    x, y, history = 0, 0, set()
    d2xy = {
        'U': (0, 1),	# x=0, y=1
        'D': (0, -1),	# x=0, y=-1
        'L': (-1, 0),	# x=-1, y=0
        'R': (1, 0),	# x=1, y=0
    }
    
    for d in dirs:
        dx, dy = d2xy[d]
        if -5 <= x+dx <= 5 and -5 <= y+dy <= 5:
            history.add((x, y, x+dx, y+dy))
            history.add((x+dx, y+dy, x, y))
            x += dx
            y += dy
        
    return len(set(history)) // 2