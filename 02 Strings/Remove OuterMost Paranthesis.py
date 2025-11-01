def removeOuterParentheses(s: str) -> str:
    cnt = 0
    ans = ""

    for ch in s:
        # If closing bracket, reduce count first
        if ch == ')':
            cnt -= 1

        # Only add character if it's NOT part of the outermost layer
        if cnt != 0:
            ans += ch

        # If opening bracket, increase count after adding
        if ch == '(':
            cnt += 1

    return ans

print(removeOuterParentheses("(()())(())"))      # Output: ()()()
print(removeOuterParentheses("(()())(())(()(()))")) # Output: ()()()()(())
