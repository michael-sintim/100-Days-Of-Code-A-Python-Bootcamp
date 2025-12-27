#love challenge

x = input("What's your name: ").lower()
y = input("What's your crush's name: ").lower()

w = x+y


f = w.count('t')
g = w.count('r')
h = w.count('u')
i = w.count('e')

j = f+g+h+i

k = w.count('l')
l = w.count('o')
m = w.count('v')
n = w.count('e')

c = k+l+m+n



print('T occured',f,'times')
print('r occured',g,'times')
print('u occured',h,'times')
print('e occured',i,'times')
print(f"total = {j}")


print('L occured',k,'times')
print('o occured',l,'times')
print('v occured',m,'times')
print('e occured',n,'times')
print(f"total = {c}")
print(f"total percentage= {j}{c}%")

z= str(j)+ str(c)
print(z)


if int(z) < 10  or int(z) > 90:
    print(f'Your score is {z}, you go together like coke and mentos')

elif 40 < int(z) < 50:
    print(f'Your score is {z}, you are alright together')

else: 
    print(f'Your score is {z}')
    








