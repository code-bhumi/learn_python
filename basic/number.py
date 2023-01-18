# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
a = int(input("what's a? "))
b = int(input("what's b? "))

x = (a * b)
if x <= 1000:
    print(x)

else:
    print(a + b)
   