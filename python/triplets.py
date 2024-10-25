def triplets(numbers):
    triplets = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            for k in range(j+1, len(numbers)):
                if(numbers[i] + numbers[j] + numbers[k] == 0):
                    triplets.append([numbers[i], numbers[j], numbers[k]])

    return triplets

nums = [-1,0,1,2,-1,-4]
print(triplets(nums))