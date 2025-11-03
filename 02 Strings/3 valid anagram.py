def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    for i in s:
        a1 = s.count(i)
        a2 = t.count(i)
        if a1 != a2:
            return False
    else:
        return True
s = "egg"
t = "add"
print(isIsomorphic(s, t))  
