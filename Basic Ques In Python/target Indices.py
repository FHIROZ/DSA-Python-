def targetIndices(nums, target):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if nums[i] == target:
            result.append(i)
    return result
nums = [1, 2, 5, 2, 3]
target = 2
print(targetIndices(nums, target))
