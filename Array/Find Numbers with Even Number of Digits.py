nums = [12,345,2,6,7896]
l=[]
for i in nums:
    l.append(str(i))
print(l)
count=0
for i in l:
    a=len(i)
    if a%2==0:
        count+=1
print(count)
