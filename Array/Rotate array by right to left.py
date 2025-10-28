def rotateArr(arr, k):
    k = k % len(arr)   # handle if k > len(arr)
    arr[:] = arr[k:] + arr[:k]
    return arr


arr = [1, 2, 3, 4, 5]
k = 2
print(rotateArr(arr, k))
 