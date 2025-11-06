from collections import defaultdict

def frequencySort(s: str) -> str:
    freq = defaultdict(int)
    for i in s:
        freq[i] += 1
    sorted_list = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    result = ''.join(char * count for char, count in sorted_list)
    return result
s = "tree"
print(frequencySort(s))
