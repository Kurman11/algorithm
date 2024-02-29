from collections import deque

def solution(cacheSize, cities) :
    answer = 0
    data = deque()

    if cacheSize == 0 :
        return len(cities) * 5

    for city in cities :
        city = city.lower()
        if city in data :
            answer += 1
            data.remove(city)
        else :
            answer += 5
            if len(data) >= cacheSize :
                data.popleft()
        data.append(city)

    return answer