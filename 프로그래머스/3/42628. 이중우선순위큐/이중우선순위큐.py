import heapq
def solution(operations):
    answer = []
    q=[]
    for o in operations:
        command,num=o.split()
        num=int(num)
        if command=='I':
            heapq.heappush(q,num)
        else:
            if q:
                if num==1:  #최댓값삭제
                    q.pop(q.index(heapq.nlargest(1,q)[0]))
                elif num==-1:  #최솟값삭제
                    heapq.heappop(q)    
            else:
                continue
    if len(q)==0:
        return [0,0]
    else:
        return [heapq.nlargest(1,q)[0],heapq.nsmallest(1,q)[0]]