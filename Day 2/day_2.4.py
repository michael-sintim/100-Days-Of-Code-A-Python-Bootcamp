#your life in weeks days months x   from 90

def age_calculator():
    old_age = 90
    age = float(input("Enter your age: "))
    age_in_weeks = (90*52) - (age*52)
    age_in_days = (90*365) - (age*365)
    age_in_months = (90*12) - (age*12)

    return f"You are {age_in_weeks} weeks from 90\nYou are {age_in_days} days from 90 \nYou are {age_in_months} months from 90"

print(age_calculator())