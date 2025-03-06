#!/usr/bin/python3

def sorted_score_list(score):
    '''students = [
        ("Alice", 85),
        ("Bob", 92),
        ("Charlie", 78),
        ("David", 90),
        ("Eva", 95),
        ("Frank", 65)
    ]'''
    
    sorted_list = sorted(score, key=lambda x:x[1], reverse=True)
    return sorted_list
    '''
    students.sort(key=lambda x:x[1], reverse=True)
    print(s)'''

'''if __name__ == '__main__':
   students = [
        ("Alice", 85),
        ("Bob", 92),
        ("Charlie", 78),
        ("David", 90),
        ("Eva", 95),
        ("Frank", 65)
    ]
print(sorted_score_list(students))'''
