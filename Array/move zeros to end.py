def move_zeros(arr):
    val=0
    for i in arr:
        if i==0:
            arr.remove(i)
            arr.append(val)
    return arr
arr=[1,0,8,4,0,7,0,5]
print(move_zeros(arr))