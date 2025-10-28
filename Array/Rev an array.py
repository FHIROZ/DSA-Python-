arr=[1,2,3,4,5]  # for below all --> o(n)

# print(arr[::-1])
#------------------------------------------
# arr.reverse()
# print(arr)
#-------------------------
#print(list(reversed(arr)))
#--------------------------------
l=[]
for i in range(len(arr)-1,-1,-1):
    l.append(arr[i])
print(l)
    