#Pedro Gallino
#11/12/17
#listDemo.py - print out first and last words in a list

words = input('Enter some words:').split(' ')

# to print out the list one item per line
for w in words:
    print(w)
    
print('the first word was',words[0])
print('the last word was', words[-1])