# 1732
def Altitude(gain):
    maximum=0
    arr=[0]
    for i in gain:
        maximum=maximum+i
        arr.append(maximum)
    return max(arr)
gain=[-5,1,5,0,-7]
result=Altitude(gain)
print(result)