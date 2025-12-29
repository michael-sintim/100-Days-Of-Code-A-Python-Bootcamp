import random

def password_generator():
    letters = int(input("How many letters would you like in your password: "))
    symbols = int(input("How many symbols would you like in your password: "))
    numbers = int(input("How many numbers would you like in your password: "))

    a_z = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z'
    ]

    A_Z = [
        'A','B','C','D','E','F','G','H','I','J','K','L','M',
        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
    ]

    symbols_c = [
        '!','@','#','$','%','^','&','*','(',')','_','+',
        '-','=','{','}','[',']','|','\\',':',';','"',"'",'<','>','?','/','.'
    ]

    digits = ['0','1','2','3','4','5','6','7','8','9']

    password_list = []


    for _ in range(letters):
        password_list.append(random.choice(a_z))

    for _ in range(letters):
        password_list.append(random.choice(A_Z))

    for _ in range(symbols):
        password_list.append(random.choice(symbols_c))

    for _ in range(numbers):
        password_list.append(random.choice(digits))

    random.shuffle(password_list)

    password = ''.join(password_list)
    return password
