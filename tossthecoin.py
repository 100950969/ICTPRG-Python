import random

def cointoss(number):
    print('Toss the Coin')
    guess = 10
    list1 = []
    while guess < 10:
        coin = random.randint(1,2)
        if (coin == 1):
            print('Heads')
            list1.append('Heads')
        elif (coin == 2):
            print('Tails')
            list1.append("Tails")

        guess += 1

    if guess > 7:
        print('Game Over')
        print(list1)

    print('Hello World')
    


# while guess < 10:
#     print("The flip is showing ", )
