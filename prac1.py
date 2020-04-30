import random

print("Hey there! Lets play a little guessing game.")
print("Guess the number between 0 and 25")

answer  = random.randint(0, 25)
guess = 0
gleft = 6
guesslog = []

while guess <  7:
    num1 = int(input('Enter Guess: '))
    guesslog.append(num1)

    if num1 == answer:
        print('Damn you win!')
        print('The number was', answer)
        print('You guessed in', guess + 1, 'guesses')
        print('Your guess log:')
        print(guesslog)
        break

    elif num1 < answer:
        print('Your guess was to low!')
        print('You have ', gleft, " left")
    
    elif num1 > answer:
        print('Your guess was to high')

        print('You have ', gleft, " left")

    guess += 1
    gleft -= 1

if guess >= 7:
    print('AHAHA You lose!!')
    print('The number was ', answer)
    print('Your guess log:')
    print(guesslog)
