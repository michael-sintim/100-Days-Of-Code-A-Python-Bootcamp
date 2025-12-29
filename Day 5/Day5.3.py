student_scores = input("Input a list of students scores: ").split()
for n in range(0,len(student_scores)):

    student_scores[n]=int(student_scores[n])

x = max(student_scores)
print(f"The max score is {x}")
