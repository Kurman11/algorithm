N, K = map(int ,input().split())
num_list = list(map(int ,input().split()))

cnt = 0
result = -1
def merge_sort(num_list, p, r):
    if p < r and cnt <= K:
        q = (p + r) // 2
        merge_sort(num_list, p, q)
        merge_sort(num_list, q + 1, r)
        merge(num_list, p, q, r)
def merge(num_list, p, q, r):
    i = p
    j = q + 1
    t = 1
    tmp = []
    global cnt, result
    while i <= q and j <= r:
        if num_list[i] <= num_list[j]:
            tmp.append(num_list[i])
            i += 1
        else:
            tmp.append(num_list[j])
            j += 1
    while i <= q:
        tmp.append(num_list[i])
        i += 1
    while j <= r:
        tmp.append(num_list[j])
        j += 1
    i = p
    t = 0
    while i <= r:
        num_list[i] = tmp[t]
        cnt += 1
        if cnt == K:
            result = num_list[i]
            break
        i += 1
        t += 1

merge_sort(num_list, 0, N-1)
print(result)