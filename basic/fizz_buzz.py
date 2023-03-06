""" Write a function called fizz_buzz that takes a number.

    If the number is divisible by 3, it should return “Fizz”.
    If it is divisible by 5, it should return “Buzz”.
    If it is divisible by both 3 and 5, it should return “FizzBuzz”.
    Otherwise, it should return the same number.
"""
def game_fizz_buzz():        
    num = int(input())
    print(f'num == {num}')
    
    if num % 3 == 0 and num % 5 == 0:
        print(f'{num} you are FizzBuzz...')
    elif num % 3 == 0:
        print(f'{num} you are Fizz...')
    elif num % 5 == 0:
        print(f'{num} you are Buzz...')
    else:
        print(f'{num}')

if __name__ == "__main__":
    game_fizz_buzz()
        