def Rotate_string(s,goal):
    if(len(s)!=len(goal)):
        return False
    n=len(s)
    for k in range(n):
        if s[k:]+s[:k]==goal:
            return True
    return False           
s="hello"
goal="bcdea"
result=Rotate_string(s,goal)
print(result) 