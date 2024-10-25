from copy import deepcopy

original_list = [[1, 2, 3], [4, 5, 6]]

# Using copy module for deep copy
deep_copy_list = deepcopy(original_list)

# Modifying an element in the deep copy does not affect the original
deep_copy_list[0][0] = 99
print(original_list)       # Output: [[1, 2, 3], [4, 5, 6]]
