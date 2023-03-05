def date_time():
    import datetime
    
    now = datetime.datetime.now()
    print("current date and time :")
    print(now.strftime("%y-%m-%d %H:%M:%S "))
    
if __name__ == '__main__':
    date_time()    