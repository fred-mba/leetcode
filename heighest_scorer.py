#!/usr/bin/python3

students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 90),
    ("Eva", 95),
    ("Frank", 65)
]
"""
top_scorer, heighest_score = students[0]

for student, score in students[1:]:
    if score > heighest_score:
        top_scorer, heighest_score = student, score
print('{}, {}'.format(top_scorer, heighest_score))

"""
heighest = max(students, key=lambda x:x[1])
print(f'{heighest}')
