def sum_closest(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(1, n-1):
            if(i!=j):
                if(numbers[i] + numbers[j] == 0 or numbers[i] + numbers[j] == 1):
                    print('The 2 numbers closest to 0 are:', numbers[i], ' and ', numbers[j],' distance=', numbers[i] + numbers[j] )
                    return

print('Array:', [-23, 12, -35, 45, 20, 36])
sum_closest([-23, 12, -35, 45, 20, 36])