def times_table():
    num = int(input("which times table do you want me to print..."))
    for i in range(1,11):
        solution = num * i 
        print(solution)

if __name__ == '__main__':
    times_table()      