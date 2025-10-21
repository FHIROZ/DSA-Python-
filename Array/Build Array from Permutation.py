# LeetCode Problem 1920: Build Array from Permutation

# Given nums, build an array ans such that ans[i] = nums[nums[i]]

nums = [0, 2, 1, 5, 3, 4]   
ans = []

for i in range(len(nums)):
    ans.append(nums[nums[i]])

print(ans)   # Output: [0, 1, 2, 4, 5, 3]
