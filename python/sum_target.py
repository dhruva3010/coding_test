def print_sum_index(arr, target):
    arr_len = len(arr)
    
    is_got_result = False
    for i in range(arr_len):
        if is_got_result:
            break
        for j in range(i + 1, arr_len):
            sum = arr[i] + arr[j]
            if sum == target:
                print(f"Indexes are {i} & {j} whose sum is {sum} and the nos are {arr[i]} & {arr[j]}")
                is_got_result = True
                break

print_sum_index([5, 6, 13, 15, 7, 1, 2], 13)
