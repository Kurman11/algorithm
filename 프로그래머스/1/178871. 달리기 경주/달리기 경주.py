def solution(players, callings):

    playerDic = { player : rank for rank, player in enumerate(players) }

    for calling in callings:
        pre, index = playerDic[calling] - 1 , playerDic[calling]  # 앞사람 인덱스, 불린사람 인덱스
        players[pre], players[index] = players[index], players[pre]  # 배열 순서 바꾸기
        playerDic[players[pre]] -= 1   # 딕셔너리 값 변경  # 배열 바뀐것 주의
        playerDic[players[index]] += 1
    
    return players