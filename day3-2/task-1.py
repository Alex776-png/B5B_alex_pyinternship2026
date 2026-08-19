def marks_summary(marks):
    lowest = min(marks)
    highest = max(marks)
    average = sum(marks) / len(marks)
    return lowest, highest, average


marks = [78, 85, 92, 67, 88]

lowest, highest, average = marks_summary(marks)

print("Lowest:", lowest)
print("Highest:", highest)
print("Average:", average)