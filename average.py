#!/usr/bin/python3

def moderate(students):
    '''students = [
        ("Alice", 85),
        ("Bob", 92),
        ("Charlie", 78),
        ("David", 90),
        ("Eva", 95),
        ("Frank", 65)
    ]
    total = 0

    for _, score in students:
        total += score
        average = float(total / len(students))
    print('{:.2f}'.format(average))
    '''
    average = sum(score for _, score in students) / len(students)
    
    return average


"""if __name__ == "__main__":
    students = [
        ("Alice", 85),
        ("Bob", 92),
        ("Charlie", 78),
        ("David", 90),
        ("Eva", 95),
        ("Frank", 65)
    ]
    print(f'{moderate(students):.2f}')"""
