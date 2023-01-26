'''
    1. start 2 letters
    2. length 2 - 6
    3. number cannot start with 0
    4. no char other than number or A-Z
'''

import re

def validate_vanity_plates(plate_number):
    if len(plate_number) < 2 or len(plate_number) > 6:
        print(f'error: length cannot be less than 2 or greather than 6 | length == {len(plate_number)}')
        return False
    if plate_number[0].isupper() == False or plate_number[1].isupper() == False:
        print(f'error: first two chars must be A-Z')
        return False
    if (len(plate_number) == 2):
        return True
    for c in plate_number:
        if (c.isdigit() or c.isalpha()) == False:
                print(f'error: plate number must be num or alpha == {plate_number}')
                return False  
    m = re.search(r"\d", plate_number)
    if m:
        pos = m.start()
        num = plate_number[pos:]
        if num.isdigit() == False or num[0] == '0':
            print(f'error: num is not valid num == {num}')
            return False
    else:
        print(f'error: no number found in the number plate == {plate_number}')
        return
    return True
    
if __name__ == '__main__':
    print('---------------------------------------------------------------------')
    print(validate_vanity_plates('sDBG1'))
    print('---------------------------------------------------------------------')
    print(validate_vanity_plates('aD1254'))
    print('---------------------------------------------------------------------')
    print(validate_vanity_plates('AD 325'))  # error in this one
    print('---------------------------------------------------------------------')
    print(validate_vanity_plates('SE0254'))
    print('---------------------------------------------------------------------')
    print(validate_vanity_plates('AS'))      # error in this one
    print('---------------------------------------------------------------------')
    print(validate_vanity_plates('AD.256'))  # error in this one
    print('---------------------------------------------------------------------')
    print(validate_vanity_plates('ER@G25'))  # error in this one
    print('---------------------------------------------------------------------')
