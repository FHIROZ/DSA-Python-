# LeetCode Problem 1929: Concatenation of Array

nums = [1, 2, 1]  
ans = []

# Append nums twice
for i in nums:
    ans.append(i)
for i in nums:
    ans.append(i)

print(ans)   # Output: [1, 2, 1, 1, 2, 1]
  

'''
nums = [1, 2, 1]
ans = nums + nums
print(ans)   # Output: [1, 2, 1, 1, 2, 1]
'''