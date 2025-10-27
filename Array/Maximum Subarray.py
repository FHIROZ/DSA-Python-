def maxi_subarray(nums):
    maxi=min(nums)
    sum=0
    for i in range(len(nums)):
        sum=sum+nums[i]
        if sum>maxi:
            maxi=sum
        if sum<0:
            sum=0
    return maxi
nums = [-2,1,-3,4,-1,2,1,-5,4]
result=maxi_subarray(nums)
print(result)