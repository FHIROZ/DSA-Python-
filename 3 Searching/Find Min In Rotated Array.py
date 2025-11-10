def Find_pivot(arr):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=start+(end-start)//2
        if(mid<end and arr[mid]>arr[mid+1]):
            return arr[mid+1]
        if(arr[mid]<arr[mid-1]):
            return arr[mid]
        elif(arr[start]<arr[mid]):
            start=mid+1
        else:
            end=mid-1
    return arr[0]


arr=[11,12,13]
res=Find_pivot(arr)
print(res)