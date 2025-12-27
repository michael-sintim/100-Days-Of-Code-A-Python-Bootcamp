#BMI calculator

def Bmi_calculator():
    gender = input("Enter your gender [M/F]")
    weight_in_kg = float(input("Enter your weight in Kg: "))
    height_in_m = float(input("Enter your height in m: "))
    # weight_in_lbs = float(input("Enter your weight in lbs: "))
    # height_in_in = float(input("Enter your height in in: "))
    male = ['M','m','male','Male']
    female = ['f','F','Female','female']
    BMI = weight_in_kg/height_in_m**2

    if gender in male and 0 <= BMI < 18.5:
        return 'Underweight'
    
    elif gender in male and 18.5 <= BMI <= 24.9 :
        return 'Normal'
    
    elif gender in male and 25.0 <= BMI <= 29.9:
        return 'Overweight'
    
    elif gender in male and 30.0 <= BMI <= 34.9:
        return 'Obese (Class I)'
    
    elif gender in male and 35.0 <= BMI <= 39.9:
        return 'Obese (Class II)'
    
    
    if gender in female and 0 <= BMI < 18.5:
        return 'Underweight'
    
    elif gender in female and 18.5 <= BMI <= 24.9 :
        return 'Normal'
    
    elif gender in female and 25.0 <= BMI <= 29.9:
        return 'Overweight'
    
    elif gender in female and 30.0 <= BMI <= 34.9:
        return 'Obese (Class I)'
    
    elif gender in female and 35.0 <= BMI <= 39.9:
        return 'Obese (Class II)'
    
    else:
        return 'Obese (Class III)'
    
    
    
print(Bmi_calculator())