def Linear_search(arr,target):
    for i in arr:
        if i==target:
            return True
    else:
        return False
arr=[1,2,3,4,5]
target=30
result=Linear_search(arr,target)
print(result)
