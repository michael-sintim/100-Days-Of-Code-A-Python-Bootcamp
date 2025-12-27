import random

#randomly choosing an individual to pay bills
x = []

y= input("Name everyone present: ")
z= y.split(",")

q= random.choice(z)
print(f"{q} is paying the billtoday")

