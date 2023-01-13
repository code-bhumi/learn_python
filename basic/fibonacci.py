def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    c = a + b
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return c

if __name__ == '__main__':
    for i in range(101):
        print(f'{fibo(i)} ', end='')
    print('')