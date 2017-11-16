#Pedro Gallino
#11/16/17
#warmUp13.py - prints the min max sum of a list of random numbers

nums = []
from random import randint
for k in range(1,21):
    i = randint(-100,100)
    nums.append(i)

nums.sort()
print('The max is',nums[-1])
print('The minimum is',nums[0])
print('The sum is',sum(nums))

