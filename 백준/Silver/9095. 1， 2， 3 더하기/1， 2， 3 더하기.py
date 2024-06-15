def count_ways(target, numbers, current_sum=0, index=0):
    if current_sum == target:
        return 1
    if current_sum > target:
        return 0

    ways = 0
    for i in range(len(numbers)):
        ways += count_ways(target, numbers, current_sum + numbers[i], i)

    return ways

n = int(input())
numbers = [1, 2, 3]
for i in range(n):
    target_value = int(input())
    result = count_ways(target_value, numbers)
    print(result)