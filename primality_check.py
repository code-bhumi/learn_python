import math
import random

def is_prime_fast(n):
   for i in range(2, int(math.sqrt(n)) + 1):
      if n % i == 0:
         return False
   return True      

def is_prime_normal(n):
   for i in range(2, n):
      if n % i == 0:
         return False
   return True

def test_1():
   for i in range(20):
      n = random.randint(1, 1000)
      if is_prime_normal(n):
         print(f'{n} is a prime number')
      else:
         print(f'{n} is NOT a prime number')

def test_2():
   n = 1
   while n != 0:
      n = int(input())
      if is_prime_normal(n):
         print(f'{n} is a prime number')
      else:
         print(f'{n} is NOT a prime number')
         
def test_3():
   for i in range(2, 30):
      print(f'{i} == {is_prime_normal(i)} {is_prime_fast(i)}')
      
def test_4():
   assert(True == is_prime_fast(2))
   assert(False == is_prime_fast(10))

if __name__ == '__main__':
   #test_1()
   #test_2()     
   #test_3()
   test_4()