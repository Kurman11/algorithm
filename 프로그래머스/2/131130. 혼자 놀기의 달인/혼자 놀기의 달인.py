def solution(cards):
    length = len(cards)
    visited = [False]*length
    box = list()
    
    for i in range(length) :
        if not visited[i] :
            idx = i
            cnt = 0
            while not visited[idx] :
                cnt += 1
                visited[idx] = True
                idx = cards[idx] - 1
            box.append(cnt)
    box.sort(reverse = True)
    box.append(0)
    
    return box[0]*box[1]