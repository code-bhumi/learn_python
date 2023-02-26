def find_information(file_name, name):
    with open(file_name, 'r') as fh:
        n = name.split(' ')
        for x in fh:
            a = x.split(' ')
            if a[1] == n[0] and a[2] == n[1]:
                a[3] = a[3].replace('\n', '').replace('\r', '')
                print(f'{a[1]} {a[2]} has {a[0]} roll number is {a[3]} years old')
        fh.close()

if __name__ == '__main__':
    find_information('students.txt', 'atharv kumar')