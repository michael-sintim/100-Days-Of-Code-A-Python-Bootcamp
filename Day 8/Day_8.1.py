student_grades = {
    'Ama': 69,
    'Kofi': 87,
    'domm': 67,
    'kow': 95,

}

for student in student_grades:
    score =  student_grades[student]
    if score > 90:
        student_grades[student] = 'Outstanding'

    elif score > 80: 
        student_grades[student] = 'Exceeds Expectations'

    elif score > 70: 
        student_grades[student] = 'Acceptable'

    else:
        student_grades[student] = 'Fail'

print(student_grades)


##

