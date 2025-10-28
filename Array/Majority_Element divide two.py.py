

def Majority_Element(nums):
    count=0
    candidate=None
    for num in nums:
        if count==0:
            candidate=num
            count=1
        elif candidate==num:
            count+=1
        else:
            count-=1
    total=0
    for number in nums:
        if number==candidate:
            total+=1
    if total>len(nums)//2:
        return candidate
    else:
        return -1

arr = [3,2,3]
res=Majority_Element(arr)
print(res)