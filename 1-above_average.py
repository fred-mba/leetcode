#!/usr/bin/python3


students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 90),
    ("Eva", 95),
    ("Frank", 65)
]

Average = sum(scores for _, scores in students) / len(students)

Above_average = [student for student in students if student[1] > Average]

sorted_above_average = sorted(Above_average, key=lambda x:x[1], reverse=True)

print(sorted_above_average)
