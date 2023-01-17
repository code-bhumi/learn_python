'''
    Description: this program generates random array of n numbers
    Author: Meenakshi Pal
    Date: 17/01/2023
'''
import random

def random_array(n):
    v = []
    for i in range(1, n + 1):
        v.append(i)
    
    for i in range(n - 1, -1, -1):
        ind = random.randint(0, i)
        if ind != i:
            v[ind], v[i] = v[i], v[ind]
    return v

if __name__ == '__main__':
    v = random_array(100)
    print(v)