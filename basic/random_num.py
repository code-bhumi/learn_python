import random

def random_array(n):
    v = []
    for i in range(1, n + 1):
        v.append(i)
    print(v)
    
    for i in range(n - 1, -1, -1):
        index = random.randint(0, i)
        if index != i:
            v[index], v[i] = v[i], v[index]
    return v

if __name__ == '__main__':
    v = random_array(10)
    print(v)