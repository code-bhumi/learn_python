list1 = [5,3,6,4,17,2,10,13,9,25,19,36,41,28,16,34]
list2 = [4,6,9,8,12,15,23,27,16,13,10,19,36,2,34,61]

list3 = []

for i in list1:
    if i in list2:
        list3.append(i)
        
print(list3)    