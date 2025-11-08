def Search(nums,target):
    start=0
    end=len(nums)-1
    while(start<=end):
        mid=start+(end-start)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return start
arr=[1,2,3,4,5]
target=30
result=Search(arr,target)
print(result)