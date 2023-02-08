import random

def guessing_game():
    computer = random.randint(1, 10)
    for i in range(10):  
        user = int(input("guess a number between 1 to 10 " ))
        if computer == user:
            print('Hurray you guess exactly right')
            break    
        elif user <= computer:
            print('sorry you guess too low try again...')
        elif user >= computer:
            print('sorry you guess too high try again...')    

guessing_game()        