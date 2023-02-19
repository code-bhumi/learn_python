import random

def game():
    number = str(random.randrange(1000,9999))
    user   = str(input("guess a four digit number? "))
    print(f'computer number = {number} and user number = {user}')
    
    if number == user:
        print('you win')
        return

    cows = 0
    bulls = 0
    for i in range(len(number)):
        if number[i] == user[i]:
            cows += 1
        else:
            bulls += 1
    print(f'number of cows = {cows} and bulls = {bulls}')

if __name__ == '__main__':
    game()

