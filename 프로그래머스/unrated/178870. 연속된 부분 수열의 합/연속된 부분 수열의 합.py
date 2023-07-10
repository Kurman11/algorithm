def solution(sequence, k):
    answer = []
    prefix_sum = 0
    prefix_sums = {0: -1}  # Store prefix sums and their corresponding indices
    result = []
    min_length = float('inf')

    for i in range(len(sequence)):
        prefix_sum += sequence[i]
        
        if prefix_sum - k in prefix_sums:
            start = prefix_sums[prefix_sum - k] + 1
            end = i
            length = end - start + 1

            if length < min_length:
                min_length = length
                result = [start, end]

        prefix_sums[prefix_sum] = i

    return result