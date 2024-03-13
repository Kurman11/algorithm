def solution(N, stages):
    stages.sort()
    # print(stages)
    failLst = []
    # 1부터 n까지의 스테이지에 대한 실패율 구하기
    for i in range(1, N+1):
        # i의 개수 카운트 
        count = stages.count(i)
        # 분모가 0일 때(ZeroDivisionError) 처리
        failure = count/len(stages) if len(stages) != 0 else 0 
        failLst.append((failure, i))
        stages = stages[count:]
    
    failLst.sort(key=lambda x:-x[0])
    failLst = [x[1] for x in failLst]
    return failLst