from typing import List
def final_value_after_operations(operations: List[str]) -> int:
    x = 0
    for op in operations:
        if "+" in op:
            x += 1
        else:
            x -= 1
    return x
operations = ["--X", "X++", "X++"]
result = final_value_after_operations(operations)
print(result)
