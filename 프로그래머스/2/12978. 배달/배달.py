from collections import deque
def solution(N, road, K):
    cache = [ float("inf") for _ in range(N+1)]
    cache[1] = 0
    queue = deque([(1, 0)])
    while queue:
        curr, total = queue.popleft()
        for a, b, w in road:
            new_total = total + w
            if a == curr and new_total < cache[b]:
                cache[b] = new_total
                queue.append((b, new_total))
            elif b == curr and new_total < cache[a]:
                cache[a] = new_total
                queue.append((a, new_total))
    return len([x for x in cache if x <= K])