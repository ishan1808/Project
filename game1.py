import random
b=['Rock','Paper','Scissors']

# Display game rules
print('WELCOME TO THE GAME OF ROCK PAPER SCISSORS')
print('<< User Vs Computer Edition >>')
print("Winning Rules:")
print("Rock vs Paper -> Paper wins")
print("Rock vs Scissors -> Rock wins")
print("Paper vs Scissors -> Scissors wins\n")

while True:
    print('1 - Rock\n2 - Paper\n3 - Scissors')

    # User input
    try:
        x=int(input('Enter your choice (1-3): '))
        if x<1 or x>3:
            print('Enter number only in between 1 and 3!!!')
            continue
    except:
        print('Enter only number!!!')
        continue
    # Computer choice
    y=random.randint(1,3)

    # Determine winner
    print(f'{b[x-1]} vs {b[y-1]}')

    if x==y:
        print('Its a draw !!!')

    elif (x==1 and y==3) or (x==2 and y==1) or (x==3 and y==2):
        print('Congrats!!! You won!!!')

    else:
        print('You lose!!! System wins...')
   
    # Play again
    a=input('Do you want to play again? Y/N: ')
    if a.upper() == 'Y':
        continue
    else:
        break

print("\nThanks for playing!")