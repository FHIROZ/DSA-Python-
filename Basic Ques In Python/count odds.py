def countOdds(low: int, high: int) -> int:
    return (high + 1) // 2 - (low // 2)
low = int(input("Enter low value: "))
high = int(input("Enter high value: "))
result = countOdds(low, high)
print("Number of odd numbers =", result)
