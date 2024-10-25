def closestToZero(arr):
    arr.sort()  # sort the array in ascending order
    left = 0  # initialize left pointer
    right = len(arr) - 1  # initialize right pointer
    minSum = float('inf')  # initialize minSum to maximum possible value
    while left <= right:  # while left pointer is less than or equal to right pointer
        sum = arr[left] + arr[right]  # calculate sum of elements at left and right pointers
        if abs(sum) < abs(minSum):  # if absolute value of sum is less than absolute value of minSum
            minSum = sum  # update minSum
        if sum < 0:  # if sum is less than zero
            left += 1  # increment left pointer
        else:  # if sum is greater than or equal to zero
            right -= 1  # decrement right pointer
    return (arr[left], arr[right])  # return elements at left and right pointers

arr = [-1, 2, 3, -4, 5]
print(closestToZero)