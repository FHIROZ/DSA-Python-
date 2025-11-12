# 540
def Single_ElementSearch(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n - 1] != arr[n - 2]:
        return arr[n - 1]
    start = 1
    end = n - 2
    while start <= end:
        mid = (start + end) // 2        
        if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
            return arr[mid]
        if ((mid % 2 != 0 and arr[mid] == arr[mid - 1]) or 
            (mid % 2 == 0 and arr[mid] == arr[mid + 1])):
            start = mid + 1
        else:
            end = mid - 1
    return -1
arr=[1,1,2,2,3,3,4,5,5,6,6]
res=Single_ElementSearch(arr)
print(res)