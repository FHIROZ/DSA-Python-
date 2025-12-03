def search(arr, target, start, end):
    if start > end:
        return -1
    mid = start + (end - start) // 2
    if arr[mid] == target:
        return arr[mid]
    elif target < arr[mid]:
        return search(arr, target, start, mid - 1)
    else:
        return search(arr, target, mid + 1, end)
if __name__ == '__main__':
    arr = [2, 3, 5, 7, 8, 9, 12, 34, 67, 89, 90]
    target = 34
    result = search(arr, target, 0, len(arr) - 1)
    print(result)