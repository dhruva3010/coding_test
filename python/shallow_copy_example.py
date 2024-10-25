from copy import copy

original_list = [[1, 2, 3], [4, 5, 6]]

# Using copy module for shallow copy
shallow_copy_list = copy(original_list)

# Modifying an element in the shallow copy affects the original
shallow_copy_list[0][0] = 99
print(original_list)       # Output: [[99, 2, 3], [4, 5, 6]]
