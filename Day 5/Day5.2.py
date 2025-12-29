student_height = input("Input a list of students height: ").split()
for n in range(0,len(student_height)):

    student_height[n]=int(student_height[n])

print(student_height)

sums = sum(student_height)
total = len(student_height)
mean_height = round(sums/total)
print(f"The mean height is {mean_height}")