while True:
    usr1=input('User 1 - Rock, Paper or Scissors? ')
    usr2=input('User 2 - Rock, Paper or Scissors? ')
    if usr1 == 'Rock' and usr2 == 'Paper':
        print("User 2 Wins, would you like to play again? ")
    

    elif usr2 == 'Rock' and usr1 == 'Paper':
        print("User 1 Wins, would you like to play again? ")

    elif usr1 == 'Scissors' and usr2 == 'Paper':
        print("User 1 Wins, would you like to play again? ")

    elif usr2 == 'Scissors' and usr1 == 'Paper':
        print("User 2 Wins, would you like to play again? ")
      
    elif usr2 == 'Rock' and usr1 == 'Scissors':
        print("User 2 Wins, would you like to play again? ")

    elif usr1 == 'Rock' and usr2 == 'Scissors':
        print("User 1 Wins, would you like to play again? ")
    
    else:
        print('Please try again')

    