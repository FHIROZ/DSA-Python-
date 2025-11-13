def search(arr,target):
    row=0
    col=len(arr[0])-1
    while(row<len(arr) and col>=0):
        if(arr[row][col]==target):
            return True
        elif(arr[row][col]<target):
            row+=1
        else:
            col-=1
    return False

arr=[
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
    ]
target=300
res=search(arr,target)
print(res)