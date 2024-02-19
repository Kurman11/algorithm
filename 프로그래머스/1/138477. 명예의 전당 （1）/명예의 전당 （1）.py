import heapq

def solution(k,score):
    answer = []
    honorList = []
    for idx, s in enumerate(score):
        # k일까지는 모든 명예의 전당 등록
        if idx+1<=k:    
            heapq.heappush(honorList,s)
        # 오늘 점수가 명예의 전당 최하위 가수 점수보다 높을 경우
        elif s > honorList[0]:
            heapq.heappop(honorList)
            heapq.heappush(honorList,s)
        answer.append(honorList[0]) # min heap의 루트노드(최솟값)
    return answer