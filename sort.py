#Pedro Gallino
#11/29/17
#sort.py - does the selection sort

from random import randint
from time import time

N = 10000 #how many numbers will be sorted

"""
/* a[0] to a[n-1] is the array to sort */
 2 int i,j;
 3 int n;
 4 
 5 /* advance the position through the entire array */
 6 /*   (could do j < n-1 because single element is also min element) */
 7 for (j = 0; j < n-1; j++)
 8 {
 9     /* find the min element in the unsorted a[j .. n-1] */
10 
11     /* assume the min is the first element */
12     int iMin = j;
13     /* test against elements after j to find the smallest */
14     for (i = j+1; i < n; i++)
15     {
16         /* if this element is less, then it is the new minimum */
17         if (a[i] < a[iMin])
18         {
19             /* found new minimum; remember its index */
20             iMin = i;
21         }
22     }
23 
24     if (iMin != j) 
25     {
26         swap(a[j], a[iMin]);
27     }
28 }
"""
def mySort(A):
    n = len(A)
    for j in range(0,n-1,1) : 
        iMin = j    
        for i in range(j+1,n,1):
            if A[i] < A[iMin]:
                iMin = i
        if iMin != j:
            A[j], A[iMin] = A[iMin], A[j]
    return A
    

if __name__ == '__main__':
    
    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
        
    pythonSort = sorted(numbers) #Python's sort

    #time how long your sort takes
    t1 = time()
    numbers = (mySort(numbers))
    t2 = time()
       
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')

    
    
    