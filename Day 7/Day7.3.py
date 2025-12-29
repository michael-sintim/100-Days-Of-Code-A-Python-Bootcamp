# Caesar Cipher

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

a_z = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

def encrypt(plain_text, shift_amount):
    cipher = ""  
    for letter in plain_text:
        if letter in a_z:
            position = a_z.index(letter)
            new_position = position + shift_amount
            cipher += a_z[new_position]
        else:
            cipher += letter  

    return cipher

def decrypt(cipher,shift_amount):
    plain_text = ''
    for x in cipher:
        if x in a_z:
            position =  a_z.index(x)
            new_position = position - shift_amount
            plain_text += a_z[new_position]
    
    return f"The decoded text is {plain_text}"

if direction == 'encode':
    print(encrypt(plain_text=text,shift_amount=shift))

elif direction == 'decode':
    print(decrypt(cipher=text,shift_amount=shift))