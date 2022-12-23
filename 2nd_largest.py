def slargest(numbers):
    numbers.sort()
    return numbers[-2]

print('Array:', [5,3,2,10,6])
print('Second largest in array:', slargest([5,3,2,10,6])) 
