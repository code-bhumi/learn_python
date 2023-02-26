def read_file(file_name):
    with open(file_name, 'r') as fh:
        name_count = 0
        names = {}
        for name in fh:
            name = name.replace('\n', '').replace('\r', '')
            name_count += 1
            if name in names:
                names[name] += 1
            else:
                names[name] = 1
        print(f'{name_count} names present in the file')
        print(names)
        fh.close()
        
if __name__ == '__main__':
    read_file('namelist.txt')
