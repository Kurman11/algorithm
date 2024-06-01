def solution(bandage, health, attacks):
    t, x, y = bandage
    startHP = health
    currentTime = 0
    isAlived = True
    
    # at : attack time || ad : attack damage
    for at, ad in attacks:
        # 일단 회복 시키고 때린다.
        diffTime = at - currentTime - 1
        startHP = min(health, startHP + (diffTime * x) + (diffTime // t) * y)
        if startHP <= ad:
            isAlived = False
            break
        else:
            startHP -= ad
        currentTime = at
    answer = -1
    if isAlived:
        answer = startHP
    
    return answer