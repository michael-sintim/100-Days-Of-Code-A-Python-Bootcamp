import math

def h():
    height = int(input("Enter wall height: "))
    width = int(input("Enter wall width: "))
    area = height * width
    cans_needed = math.ceil(area/5)

    return f"You need {cans_needed} cans to cover an area of {area}m squared"
print(h())