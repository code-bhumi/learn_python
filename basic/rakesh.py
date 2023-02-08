def test():
    res = 'yes'
    while res != 'no':
        print('do you want to play the game?')
        res = str(input())

if __name__ == '__main__':
    test()