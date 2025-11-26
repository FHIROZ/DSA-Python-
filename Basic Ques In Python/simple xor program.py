def xorOperation(n, start):
    x = 0
    for i in range(n):
        x ^= (start + 2*i)
    return x
n = 5
start = 0
result = xorOperation(n, start)
print("Result:", result)
