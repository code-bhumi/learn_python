def test():
    numbers = [5,6,84,9,2,5,34,14,12,54,18,16]
    x = int(input("what is x? ")) 
    
    for number in numbers:
        if number <= x:
            print(number, end=', ')
            
if __name__ == '__main__':
    test()