"""
Rock beats scissors
Scissors beats paper
paper beats rock

"""

def rock_paper_scissor():
    while True:
        options = ['rock', 'paper', 'scissor']
        player_1 = input("player_1 which option do you choose (rock, paper, scissor): " )
        player_2 = input("player_2 which option do you choose (rock, paper, scissor): " )
        
        if player_1 == 'rock' and player_2 == 'scissor' or player_1 == 'scissor' and player_2 == 'paper' or player_1 == 'paper' and player_2 == 'rock':
            print("player_1 you are a winner")  
        elif player_1 == 'scissor' and player_2 == 'rock' or player_1 == 'paper' and player_2 == 'scissor' or player_1 == 'rock' and player_2 == 'paper':
            print("player_2 you are a winner")
        elif player_1 == player_2:
            print("it's a tie")
        else:
            print("it's not a valid input please try again")
        
        if str(input('do you want to play another game yes or no?\n')) == 'no':
            print('game over')
            break
           
rock_paper_scissor()  