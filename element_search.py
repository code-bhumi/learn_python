def element_search():
    list = [3,8,9,12,35,48,65,72]
    num = int(input("tell me a number to search in the list? "))
    
  
    if num in list  :
            print(True)
    else:
            print(False)    
        
    
if __name__== '__main__':    
    element_search()
