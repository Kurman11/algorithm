def solution(sequence, k):
    answer = []
    result = 0
    start = 0
    sublist_sum = 0
    
    for end in range(len(sequence)):
        sublist_sum += sequence[end]
        
        while sublist_sum > k:
            sublist_sum -= sequence[start]
            start += 1
        
        if sublist_sum == k:
            answer.append((start, end))

    if answer:
        min_length = float('inf')
        result = None
        
        for start, end in answer:
            length = end - start
            if length < min_length:
                min_length = length
                result = (start, end)
        
        return result
    
    return None