#Pedro Gallino
#11/12/17
#middleWord.py - finds the middle word in the list

words = input('Enter a list of words:').split(' ')

x = len(words[:])
middle = x/2
print(middle//1)
if middle//1 == 0:
    print(words[middle])
else:
    print(words[middle-1],words[middle])

