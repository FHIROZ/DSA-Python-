def reverse_words(s):
    for i in s:
        a=s.split()
        rev_words=a[::-1]
        return " ".join(rev_words)
s="hello gud mrng"
res=reverse_words(s)
print(res)




