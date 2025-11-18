def count_hours_meeting_target(hours, target):
    count = 0
    for h in hours:
        if h >= target:
            count += 1
    return count
hours = [3, 5, 2, 6, 8, 1]
target = 5
result = count_hours_meeting_target(hours, target)
print("Hours meeting target:", result)
