def facto():
        factorial = 1
        num       = 5
        for i in range(2, num + 1):
               factorial *= i
        print('the factorial of', num, 'is', factorial)
        
if __name__ == '__main__':
    facto()