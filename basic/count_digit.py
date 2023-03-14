import random

def count_digits(n):
    count = 0
    while n:
        n = n // 10
        count += 1
    return count

if __name__ == '__main__':
    for _ in range(10):
        n = random.randint(1e2, 1e9)
        print(f'{n} has {count_digits(n)}')