def pattern(n):
    while n:
        for i in range(n, 0, -1):
            print(f'{i}', end=' ')
        n -= 1
        print('')

if __name__ == '__main__':
    pattern(5) 