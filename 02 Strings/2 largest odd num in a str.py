def largestOddNumber(num):
    # Traverse from the end to find the first odd digit
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 == 1:
            # return substring from start till that digit
            return num[:i + 1]
    return ""  # no odd digit found
s="549043"
res=largestOddNumber(s)
print(res)