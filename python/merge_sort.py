def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_side = arr[:mid]
        right_side = arr[mid:]

        merge_sort(left_side)
        merge_sort(right_side)

        i = j = k = 0

        while i < len(left_side) and j < len(right_side):
            if (left_side[i] < right_side[j]):
                arr[k] = left_side[i]
                i += 1
            else:
                arr[k] = right_side[j]
                j += 1
            k += 1
        
        while i < len(left_side):
            arr[k] = left_side[i]
            i += 1
            k += 1
        
        while j < len(right_side):
            arr[k] = right_side[j]
            j += 1
            k += 1

array = [2,5,6,1,3,6,1]
new_array = sorted(array)
print(new_array)