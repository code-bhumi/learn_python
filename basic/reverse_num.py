def reverse_num():
    number =  int(input("enter your favourite number "))
    reversed_num = 0
    while(number>0):
        remainder = number % 10
        reversed_num = reversed_num * 10 + remainder
        number = number//10
        
    print(reversed_num)     
       
if __name__ == '__main__':
    reverse_num()