#Pedro Gallino
#12/4/17
#quiz.py - 5th computer quiz - I will be attempting the extra credit

from random import randint


#Retruns a list with 5 random numbers between 1 and 100
def rand5():
    L = []
    for i in range(5):
        L.append(randint(1,100))
    return L

#Returns the last element in the list
def lastElement(A):
    return A[-1]

#Takes in a list of words and returns the number of charecters
def wordLengths(B):
    ch = []
    for j in B:
        chs = 0
        for k in j:
            chs += 1
        ch.append(chs)
    return ch

#Finds the biggest number in a list
def biggest(C):
    big = C[0]
    for x in C:
        if x>big:
            big = x
    return big

print(rand5())
print(lastElement(['cat','dog','rat','man']))
print(wordLengths(['the','cat','is','hungry','and','mad','also','not','very','happy']))
print(biggest([3,-1,5,9000,7000,2,1,100]))



    
