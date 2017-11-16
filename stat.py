#Pedro Gallino
#11/16/17
#stat.py - tells the min mean median mac and mode of a data set

numbers = []
print('Type a list of numbers')
print('Enter "q" when finished')

while True:
    num = input('>')
    if num == 'q':
        break
    else:
        numbers.append(float(num))

numbers.sort

mean = (sum(numbers))/(len(numbers))

print('Min:',numbers[0])
print('Mean',mean)

x = (len(numbers[:]))/2
if x//1 == 0:
    print('Median', num[x])
else:
    print('Median',numbers[middle-1],'and',numbers[middle])

print('Max:',numbers[-1])

for i in numbers:
    if theList.count(i)> mode:
        mode = theList.count(i)
print('Mode',mode)
    




