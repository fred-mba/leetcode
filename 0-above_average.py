#!/usr/bin/python3

from average import moderate
from sorted_score import sorted_score_list


students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 90),
    ("Eva", 95),
    ("Frank", 65)
]

Average = moderate(students)
#above_average = []
'''
for student, score in students:
    if score > Average:
        above_average.append((student, score)) # Store as tuples'''
above_average = list(student for student in students if student[1] > Average)
result = sorted_score_list(above_average)
            
print(result)
