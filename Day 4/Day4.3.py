#rock paper scissors 
import random 

choices = ['rock','paper','scissors']
human_choice =  input("Choose[ Rock, Paper, Scissors ]: ").lower()
cmp_choice  =  random.choice(choices)

z = print(f"Computer chose: {cmp_choice}")


if human_choice not in choices:
    print("Invalid choice")

elif human_choice == cmp_choice:
    print("Draw")

elif human_choice == 'rock' and cmp_choice == 'paper':
    print('Computer won')

elif human_choice == 'rock' and cmp_choice == 'scissors':
    print('You won')

elif human_choice == 'paper' and cmp_choice == 'rock':
    print('You won')

elif human_choice == 'paper' and cmp_choice == 'scissors':
    print('Computer won')

elif human_choice == 'scissors' and cmp_choice == 'rock':
    print('Computer won')

elif human_choice == 'scissors' and cmp_choice == 'paper':
    print('You won')