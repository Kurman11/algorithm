def solution(arr):
	# 제일 작은 수 제거
    arr.pop(arr.index(min(arr)))
    # arr이 빈 배열이라면 -1 return 
    return arr if arr else [-1]