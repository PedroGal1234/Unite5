#Pedro Gallino
#11/30/17
#warmUp15.py - inputs a list and then doubles all the numbers
from random import randint

AMOUNT = 100
org = []

def double(L):
    numbers = []
    for i in (L):
        k = i*2
        numbers.append(k)
    numbers.sort()
    return numbers

for i in range(1,AMOUNT):
    org.append(randint(1,1000))

print(double(org))