# Brute force approach

# # def Majority_Element(nums):
#     n=len(nums)
#     k=n//3
#     new_list=[]
#     for i in nums:
#         if(nums.count(i)>k):
#             if i not in new_list:
#                 new_list.append(i)
#     return new_list
#---------------------------------------------------------
# Better Approach

# def Majority_Element(nums):
    # freq={}
    # for num in nums:
    #     if num in freq:
    #         freq[num]+=1
    #     else:
    #         freq[num]=1
    # n=len(nums)//3
    # res=[]
    # for num,count in freq.items():
    #     if count>n:
    #         res.append(num)
    # return res

# ----------------------------------------------


 