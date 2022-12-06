Suppose the input is of the following form 
 

5 7 19 20

and we want separate variables to reference them. what we want is: 
 

a = 5
b = 7
c = 19
d = 20

so, we can create a function named as get_ints() as follows: 


import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())

a,b,c,d = get_ints()


When you want to take input of list of integers given in a single line

Suppose the input is of the following form
 

1 2 3 4 5 6 7 8




and we want that a single variable will hold the whole list of integers. What we want is : 
 

Arr = [1, 2, 3, 4, 5, 6, 7, 8]




So, here we will create a function named as get_list() as follows: 
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

Arr = get_ints()


When you want to take input of string

Suppose the input is of the following form 
 

GeeksforGeeks is the best platform to practice Coding.




and we want that a single reference variable will hold this string. What we want is : 
 
import sys
def get_string(): return sys.stdin.readline().strip()

string = get_string()



#code for disabling the softspace feature
print('G','F','G', sep='')

#for formatting a date
print('09','12','2016', sep='-')

#another example
print('pratik','geeksforgeeks', sep='@')

GFG
09-12-2016
pratik@geeksforgeeks

The sep parameter when used with the end parameter it produces awesome results.
 Some examples by combining the sep and end parameters.
 
print('G','F', sep='', end='')
print('G')
#\n provides new line after printing the year
print('09','12','2016', sep='-', end='\n')

print('prtk','agarwal', sep='', end='@')
print('geeksforgeeks')

GFG
09-12-2016
prtkagarwal@geeksforgeeks

Note: Please change the language from Python to Python 3 in the online ide. 
Go to your interactive python ide by typing python in your cmd ( windows ) or terminal ( linux )

import antigravity
