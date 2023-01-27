import heapq

duk = input()
heap = []
for i in range(102):
    duk_1 = list(map(str,input().split(',')))
    for x in duk_1:
        if x == '문제':
            heapq.heappush(heap,'문제')
        elif x == '고무오리':
            if heap:
                heapq.heappop(heap)
            else:
                heapq.heappush(heap,'문제')
                heapq.heappush(heap,'문제')         
        elif x == '고무오리 디버깅 끝':
            if '문제' in heap:
                print('힝구')                                        
            else:
                print('고무오리야 사랑해')                     
    if x == '고무오리 디버깅 끝':
        break