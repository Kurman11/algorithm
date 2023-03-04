# import heapq

# lst = []
# cnt =0
# a = []
# def solution(scoville, K):
#     global cnt
#     for i in scoville:
#         heapq.heappush(lst,i)
    
#     while 1:
#         first = heapq.heappop(lst)
#         if first >= K:
#             break
#         second = heapq.heappop(lst)
#         mix = first + second * 2
        
#         if mix < K:
#             cnt += 1
#             heapq.heappush(lst,mix)
#         else:
#             a.append(mix)
#             cnt += 1
        
#         if len(lst) == 0:
#             break            
#         elif cnt == len(scoville)-1:
#             cnt = -1
#             break
    
#     return cnt
    
import heapq

def solution(scoville, K):
    lst = []
    cnt = 0

    for i in scoville:
        heapq.heappush(lst, i)

    while len(lst) > 1:
        first = heapq.heappop(lst)
        if first >= K:
            break
        second = heapq.heappop(lst)
        mix = first + second * 2
        heapq.heappush(lst, mix)
        cnt += 1

    if lst[0] >= K:
        return cnt
    else:
        return -1