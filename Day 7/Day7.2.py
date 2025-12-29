#prime number checker

n = int(input("Enter a number to check: "))

def prime():
    if n <= 1:
        return f"{n} is not a prime number"
    
    for x in range(2,n):
        if n % x ==0:
            return f"{n} is not a prime number"
        
        else:
            return f'{n} is a prime number'


print(prime())