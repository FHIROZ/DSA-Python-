# decompress_rle_list.py

def decompressRLElist(nums):
    out = []
    for i in range(0, len(nums), 2):
        freq, val = nums[i], nums[i+1]
        out.extend([val] * freq)
    return out

nums = [1, 2, 3, 4]   
result = decompressRLElist(nums)
print("Input:", nums)
print("Output:", result)
