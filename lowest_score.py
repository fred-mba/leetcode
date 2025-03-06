#!/usr/bin/python3

students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 90),
    ("Eva", 95),
    ("Frank", 65)
]
'''
scorer, lowest_score = students[0]

for student, score in students[1:]:
    if score < lowest_score:
        scorer, lowest_score = student, score
print(f'{scorer}, {lowest_score}')
'''
lowest_score = min(students, key=lambda x:x[1])
print(lowest_score)
