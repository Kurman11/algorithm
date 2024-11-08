T = int(input())

for i in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # arr1 = [[] for _ in range(N)]
    arr90 = []   # 90도 회전 결과
    arr180 = []  # 180도 회전 결과
    arr270 = []  # 270도 회전 결과

    # 90도 회전 (오른쪽으로 90도)
    for j in range(N):
        s = ''.join(str(arr[k][j]) for k in range(N - 1, -1, -1))
        arr90.append(s)

    # 180도 회전
    for j in range(N - 1, -1, -1):
        s = ''.join(str(arr[j][k]) for k in range(N - 1, -1, -1))
        arr180.append(s)

    # 270도 회전 (왼쪽으로 90도)
    for j in range(N - 1, -1, -1):
        s = ''.join(str(arr[k][j]) for k in range(N))
        arr270.append(s)


    arr1 = [(arr90[q],arr180[q],arr270[q]) for q in range(N)]

    print(f'#{i}')
    for row in arr1:
        print(*row)