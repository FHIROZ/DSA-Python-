def kidsWithCandies(candies, extraCandies):
    new_list = []
    maximum = max(candies)  

    for i in range(len(candies)):
        if (candies[i] + extraCandies) >= maximum:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list



candies = [2, 3, 5, 1, 3]
extraCandies = 3
result = kidsWithCandies(candies, extraCandies)
print(result)   # [True, True, True, False, True]
