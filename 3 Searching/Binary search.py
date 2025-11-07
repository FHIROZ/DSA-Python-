def Binary_search(arr,target):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=start+(end-start)//2
        if(target==mid):
            return mid
        elif(arr[mid]<target):
            end=mid-1
        else:
            start=mid+1
    return -1

arr=[1,2,3,4,5]
target=30
result=Binary_search(arr,target)
print(result)