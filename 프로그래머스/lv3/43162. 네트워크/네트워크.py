def dfs(x, computers, visited):
    visited[x] = True
    for a,b in enumerate(computers[x]):
        if b == 1 and (not visited[a]):
            dfs(a, computers, visited)
            
def solution(n, computers):
    visited = [False] * n
    cnt = 0
    
    for i in range(n):
        if not visited[i]:
            dfs(i,computers, visited)
            cnt += 1
    return cnt

# def solution(n, computers):
#     visited = [False]*n
#     answer = 0
#     for i in range(0,n):
#         if visited[i] == False:
#             dfs(n,computers, i, visited)
#             answer += 1
            
#     return answer


# def dfs(n, computers, i, visited):
#     visited[i] = True
    
#     for x in range(0,n):
#         if visited[x] == False and computers[i][x] == True:
#            dfs(n, computers, x, visited) 
#     return visited