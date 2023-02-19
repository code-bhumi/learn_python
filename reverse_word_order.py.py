def reversewords(s):
    
    statement = s.split(" ")
    new_statement = " ".join(reversed(statement))
    return new_statement

s1 = "meenakshi love mathematics"
print(reversewords(s1))

