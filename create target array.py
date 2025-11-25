res = []
nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]
res = []
for i, v in zip(index, nums):
    res.insert(i, v)
print(res)
