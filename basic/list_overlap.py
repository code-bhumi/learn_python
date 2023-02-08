import random

x = random.sample(range(1,30), 15)
y = random.sample(range(1,30), 12)

result = [i for i in x if i in y]

print(result) 