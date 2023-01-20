word = input("tell me a word? ")
word = str(word)
reversed = word[::-1]


if word == reversed:
    print("this word is a palindrome")
    
else:
    print("this word is not a palindrome")    