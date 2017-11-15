#Pedro Gallino
#11/15/17
#randomMonth.py - print out a random month

from random import randint

months = ['January','February','March','April','May','June','July','August','September','October','November','December' ]
num = randint(1,12)

print(months[num-1])