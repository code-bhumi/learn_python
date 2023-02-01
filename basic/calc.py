import random

OPS = ['+', '-', '*', '/']

def calc(x, op, y):
    if op is '+':
        return x+y
    if op is '-':
        return x-y
    if op is '*':
        return x*y
    if op is '/':
        return x/y            

def test():
    for _ in range(10):
        x = random.randint(int(-1e6), int(1e6))
        y = random.randint(int(-1e6), int(1e6))
        op = random.randint(0, 3)
        print('----------------------------------------------------------')
        print(x, OPS[op], y)
        print(calc(x, OPS[op], y))
        print('----------------------------------------------------------')

if __name__ == '__main__':
    test()
