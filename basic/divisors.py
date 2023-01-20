num = int(input("choose a number to divide? "))
   
listrange = list(range(1, num+1))

divisorlist = []


for number in listrange:
        if num % number == 0:
             divisorlist.append(number)

print(divisorlist)       
         