def Find_pivot(nums):
    start = 0
    end = len(nums) - 1
    while start < end:
        mid = (start + end) // 2
        if nums[mid] < nums[mid + 1]:
            start = mid + 1
        else:
            end = mid

    return start



arr=[25,26,11,12,13]
res=Find_pivot(arr)
print(res)