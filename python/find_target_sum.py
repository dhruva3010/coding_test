def two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return None

# Example usage:
numbers = [2, 7, 11, 15]
target_sum = 9

result = two_sum(numbers, target_sum)
print(f"Indices of the two numbers that add up to {target_sum}: {result}")
