import random

class Teacher(object):
    pass

class Student(object):
    pass

class Class(object):
    pass

class School(object):
    pass


import random
def report():
    print('--------------------------------------------------------------------------')
    print('| KG |')
    print('Class Teacher : Rashmi')
    print('--------------------------------------------------------------------------')
    print('Studets')
    for s in ['Atharv', 'Adwita', 'Tej Walla']:
        print('--------------------------------------------------------------------------')
        print(f'Name: {s}')
        print(f'English == {random.randint(1, 100)}')
        print(f'Hindi   == {random.randint(1, 100)}')
        print(f'Maths   == {random.randint(1, 100)}')
        print(f'Science == {random.randint(1, 100)}')
        print(f'SST     == {random.randint(1, 100)}')
        print('--------------------------------------------------------------------------')
    print('--------------------------------------------------------------------------')
    
report()