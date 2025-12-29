student_scores = input("Input a list of students scores: ").split()
for n in range(0,len(student_scores)):

    student_scores[n]=int(student_scores[n])

#using for loops
score = 0
for max in student_scores:
    if max > score:
        score = max
    



# x = max(student_scores)
print(f"The max score is {score}")
