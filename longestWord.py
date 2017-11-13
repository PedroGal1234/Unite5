#Pedro Gallino
#11/12/17
#longestWord.py - finds the longest word in a list

words = input('Enter a list of words:').split(' ')
x = ""
l = 0
for w in words:
    if len(w) > l:
        l = len(w)
        x = w

print("The longest word is",x)