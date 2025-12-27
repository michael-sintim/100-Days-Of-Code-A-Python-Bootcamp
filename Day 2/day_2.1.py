# the tip calculator
print("Welcome to the tip calculator")
question = float(input('What is the total bill? '))
x= float(input("How many people to split the bill? "))
tip =float(input("By what percentage do you wanna tip? ")) * 0.01

per_person = question / x
total = (per_person * tip) + per_person

print(f"Each person pays: ${total:.2f}")