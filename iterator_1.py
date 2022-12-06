
=============|
Loop Control |
=============|
Continue Statement
------------------------
It returns the control to the beginning of the loop.

# Prints all letters except 'e' and 's' 
for letter in 'geeksforgeeks': 
	if letter == 'e' or letter == 's': 
		continue
	print 'Current Letter :', letter 
	var = 10

Output:

		Current Letter : g
		Current Letter : k
		Current Letter : f
		Current Letter : o
		Current Letter : r
		Current Letter : g
		Current Letter : k

Break Statement
---------------------
It brings control out of the loop

for letter in 'geeksforgeeks': 

	# break the loop as soon it sees 'e' 
	# or 's' 
	if letter == 'e' or letter == 's': 
		break

print 'Current Letter :', letter 

Output:

		Current Letter : e

Pass Statement
--------------------
We use pass statement to write empty loops. Pass is also used for empty control statement, function and classes.
# An empty loop 
for letter in 'geeksforgeeks': 
	pass
print 'Last Letter :', letter 

Output:

		Last Letter : s


==============|
Switch Case   |
==============|
# Function to convert number into string 
# Switcher is dictionary data type here 
def numbers_to_strings(argument): 
	switcher = { 
		0: "zero", 
		1: "one", 
		2: "two", 
	} 

	# get() method of dictionary data type returns 
	# value of passed argument if it is present 
	# in dictionary otherwise second argument will 
	# be assigned as default value of passed argument 
	return switcher.get(argument, "nothing") 

# Driver program 
if __name__ == "__main__": 
	argument=0
	print numbers_to_strings(argument) 

Output:

		Zero

========================
Iterator
==============

# Iterator in python is an object that is used to iterate over iterable objects 
# like lists, tuples, dicts and sets. 
# Iterator object is initialised using the iter() method. It uses the next() method 
# for iteration.

# __iter(iterable)__ method that is called for initialization of an iterator. 
# This returns an iterator object
# __next__  The next method returns the next value for the 
# iterable. When we use a for loop 
# to traverse any iterable object, internally it uses the iter() method to get an 
# iterator object 
# which further uses next() method to iterate over. This method raises a 
# StopIteration to signal the end of the iteration.

# Here is an example of a python inbuilt iterator 
# value can be anything which can be iterate 
iterable_value = 'Geeks'
iterable_obj = iter(iterable_value) 

while True: 
	try: 

		# Iterate by calling next 
		item = next(iterable_obj) 
		print(item) 
	except StopIteration: 

		# exception will happen when iteration will over 
		break

Output :

		G                                                                                                                                                                            
		e                                                                                                                                                                            
		e                                                                                                                                                                            
		k                                                                                                                                                                            
		s

# A simple Python program to demonstrate 
# working of iterators using an example type 
# that iterates from 10 to given value 

# An iterable user defined type 
class Test: 

	# Cosntructor 
	def __init__(self, limit): 
		self.limit = limit 

	# Called when iteration is initialized 
	def __iter__(self): 
		self.x = 10
		return self

	# To move to next element. In Python 3, 
	# we should replace next with __next__ 
	def __next__(self): 

		# Store current value ofx 
		x = self.x 

		# Stop iteration if limit is reached 
		if x > self.limit: 
			raise StopIteration 

		# Else increment and return old value 
		self.x = x + 1; 
		return x 

# Prints numbers from 10 to 15 
for i in Test(15): 
	print(i) 

# Prints nothing 
for i in Test(5): 
	print(i) 


Output :

		10
		11
		12
		13
		14
		15

# Sample built-in iterators 

# Iterating over a list 
print("List Iteration") 
l = ["geeks", "for", "geeks"] 
for i in l: 
	print(i) 
	
# Iterating over a tuple (immutable) 
print("\nTuple Iteration") 
t = ("geeks", "for", "geeks") 
for i in t: 
	print(i) 
	
# Iterating over a String 
print("\nString Iteration")	 
s = "Geeks"
for i in s : 
	print(i) 
	
# Iterating over dictionary 
print("\nDictionary Iteration") 
d = dict() 
d['xyz'] = 123
d['abc'] = 345
for i in d : 
	print("%s %d" %(i, d[i])) 

Output :

		List Iteration
		geeks
		for
		geeks

		Tuple Iteration
		geeks
		for
		geeks

		String Iteration
		G
		e
		e
		k
		s

		Dictionary Iteration
		xyz  123
		abc  345

At many instances, we get a need to access an object like an iterator. One way is to form a 
generator loop but that extends the task and time taken by the programmer. 
Python eases this task by providing a built-in method __iter__() for this task.

The __iter__() function returns an iterator for the given object (array, set, tuple etc. or custom objects). 
It creates an object that can be accessed one element at a time using __next__() function, 
which generally comes in handy when dealing with loops.

Syntax :

iter(object)
iter(callable, sentinel)

Object : The object whose iterator has to be created. It can be a collection object like list or 
tuple or a user-defined object (using OOPS).

Callable,Sentinel : Callable represents a callable object and sentinel is the 
value at which the iteration is needed to be terminated, sentinel value represents the end of sequence being iterated.

Exception :

If we call the iterator after all the elements have 
been iterated, then StopIterationError is raised.

The __iter__() function returns an iterator object that goes through the each element of the given object. 
The next element can be accessed through __next__() function. In the case of callable object and sentinel value, 
the iteration is done until the value is found or the end of elements reached. 
In any case, the original object is not modified.

# Python code demonstrating 
# basic use of iter() 
listA = ['a','e','i','o','u'] 

iter_listA = iter(listA) 

try: 
	print( next(iter_listA)) 
	print( next(iter_listA)) 
	print( next(iter_listA)) 
	print( next(iter_listA)) 
	print( next(iter_listA)) 
	print( next(iter_listA)) #StopIteration error 
except: 
	pass


Output :

		a
		e
		i
		o
		u

# Python code demonstrating 
# basic use of iter() 
lst = [11, 22, 33, 44, 55] 

iter_lst = iter(lst) 
while True: 
	try: 
		print(iter_lst.__next__()) 
	except: 
		break
Output :

		11
		22
		33
		44
		55

# Python code demonstrating 
# basic use of iter() 

listB = ['Cat', 'Bat', 'Sat', 'Mat'] 


iter_listB = listB.__iter__() 

try: 
	print(iter_listB.__next__()) 
	print(iter_listB.__next__()) 
	print(iter_listB.__next__()) 
	print(iter_listB.__next__()) 
	print(iter_listB.__next__()) #StopIteration error 
except: 
	print(" \nThrowing 'StopIterationError'", 
					"I cannot count more.") 

Output :

		Cat
		Bat
		Sat
		Mat
		 
		Throwing 'StopIterationError' I cannot count more.

# Python code showing use of iter() using OOPs 

class Counter: 
	def __init__(self, start, end): 
		self.num = start 
		self.end = end 

	def __iter__(self): 
		return self

	def __next__(self): 
		if self.num > self.end: 
			raise StopIteration 
		else: 
			self.num += 1
			return self.num - 1
			
			
# Driver code 
if __name__ == '__main__' : 
	
	a, b = 2, 5
	
	c1 = Counter(a, b) 
	c2 = Counter(a, b) 
	
	# Way 1-to print the range without iter() 
	print ("Print the range without iter()") 
	
	for i in c1: 
		print ("Eating more Pizzas, couting ", i, end ="\n") 
	
	print ("\nPrint the range using iter()\n") 
	
	# Way 2- using iter() 
	obj = iter(c2) 
	try: 
		while True: # Print till error raised 
			print ("Eating more Pizzas, couting ", next(obj)) 
	except: 
		# when StopIteration raised, Print custom message 
		print ("\nDead on overfood, GAME OVER") 

Output :

		Print the range without iter()
		Eating more Pizzas, couting  2
		Eating more Pizzas, couting  3
		Eating more Pizzas, couting  4
		Eating more Pizzas, couting  5

		Print the range using iter()

		Eating more Pizzas, couting  2
		Eating more Pizzas, couting  3
		Eating more Pizzas, couting  4
		Eating more Pizzas, couting  5

		Dead on overfood, GAME OVER

=============|
Enumerate    |
=============|
Enumerate is built-in python function that takes input as iterator, list etc and returns a tuple 
containing index and data at that index in the iterator sequence. For example, enumerate(cars), 
returns a iterator that will return (0, cars[0]), (1, cars[1]), (2, cars[2]), and so on. 

# Accessing items using enumerate() 

cars = ["Aston" , "Audi", "McLaren "] 
for i, x in enumerate(cars): 
	print (x) 

Output :

		Aston
		Audi
		McLaren 

# Accessing items and indexes enumerate() 

cars = ["Aston" , "Audi", "McLaren "] 
for x in enumerate(cars): 
	print (x[0], x[1]) 

Output :

		(0, 'Aston')
		(1, 'Audi')
		(2, 'McLaren ')

We can also directly print returned value of enumerate() to see what it returns.

# Printing return value of enumerate() 

cars = ["Aston" , "Audi", "McLaren "] 
print enumerate(cars) 

Output :

		[(0, 'Aston'), (1, 'Audi'), (2, 'McLaren ')]

Enumerate takes parameter start which is default set to zero. We can change this parameter to any value we like. 
In the below code we have used start as 1.	

# demonstrating the use of start in enumerate 

cars = ["Aston" , "Audi", "McLaren "] 
for x in enumerate(cars, start=1): 
	print (x[0], x[1]) 

Output :

		(1, 'Aston')
		(2, 'Audi')
		(3, 'McLaren ')

enumerate() helps to embed solution for accessing each data item in the iterator and fetching index of each data item

Looping extensions:
----------------------------
Two iterators for a single looping construct: In this case, a list and dictionary are to be used 
for each iteration in a single looping block using enumerate function. Let us see example.

# Two separate lists 
cars = ["Aston", "Audi", "McLaren"] 
accessories = ["GPS kit", "Car repair-tool kit"] 

# Single dictionary holds prices of cars and 
# its accessories. 
# First three items store prices of cars and 
# next two items store prices of accessories. 
prices = {1:"570000$", 2:"68000$", 3:"450000$", 
		4:"8900$", 5:"4500$"} 

# Printing prices of cars 
for index, c in enumerate(cars, start=1): 
	print ("Car: %s Price: %s"%(c, prices[index]) )

# Printing prices of accessories 
for index, a in enumerate(accessories,start=1): 
	print ("Accessory: %s Price: %s"%(a,prices[index+len(cars)]))
		 

Output:

		Car: Aston Price: 570000$
		Car: Audi Price: 68000$
		Car: McLaren Price: 450000$
		Accessory: GPS kit Price: 8900$
		Accessory: Car repair-tool kit Price: 4500$

================|
zip function    |
================|
(Both iterators to be used in single looping construct):
This function is helpful to combine similar type iterators(list-list or dict- dict etc,) 
data items at ith position. It uses the shortest length of these input iterators. 
Other items of larger length iterators are skipped. In case of empty iterators, it returns No output.

For example, the use of zip for two lists (iterators) helped to combine a single car and its required accessory.

# Python program to demonstrate the working of zip 

# Two separate lists 
cars = ["Aston", "Audi", "McLaren"] 
accessories = ["GPS", "Car Repair Kit", 
			"Dolby sound kit"] 

# Combining lists and printing 
for c, a in zip(cars, accessories): 
	print("Car: %s, Accessory required: %s"%(c, a) )

Output:

		Car: Aston, Accessory required: GPS
		Car: Audi, Accessory required: Car Repair Kit
		Car: McLaren, Accessory required: Dolby sound kit

The reverse of these iterators from zip function is known as unzipping using “*” operator.

Use of enumerate function and zip function helps to achieve an effective extension of iteration 
logic in python and solves many more sub-problems of a huge task or problem.

# Python program to demonstrate unzip (reverse  
# of zip)using * with zip function 
  
# Unzip lists 
l1,l2 = zip(*[('Aston', 'GPS'),  
              ('Audi', 'Car Repair'),  
              ('McLaren', 'Dolby sound kit')  
           ]) 
  
# Printing unzipped lists       
print(l1) 
print(l2) 

Output:

		('Aston', 'Audi', 'McLaren')
		('GPS', 'Car Repair', 'Dolby sound kit')

===============|
Itertools      |
===============|
# Python program to demonstrate 
# iterator module 


import operator 
import time 

# Defining lists 
L1 = [1, 2, 3] 
L2 = [2, 3, 4] 

# Starting time before map 
# function 
t1 = time.time() 

# Calculating result 
a, b, c = map(operator.mul, L1, L2) 

# Ending time after map 
# function 
t2 = time.time() 

# Time taken by map function 
print("Result:", a, b, c) 
print("Time taken by map function: %.6f" %(t2 - t1)) 

# Starting time before naive 
# method 
t1 = time.time() 

# Calculating result usinf for loop 
print("Result:", end = " ") 
for i in range(3): 
	print(L1[i] * L2[i], end = " ") 
	
# Ending time after naive 
# method 
t2 = time.time() 
print("\nTime taken by for loop: %.6f" %(t2 - t1)) 

Output:

		Result: 2 6 12
		Time taken by map function: 0.000005
		Result: 2 6 12 
		Time taken by for loop: 0.000014


# Python code to illustrate generator, yield() and next(). 
def generator(): 
    t = 1
    print 'First result is ',t 
    yield t 
  
    t += 1
    print 'Second result is ',t 
    yield t 
  
    t += 1
    print 'Third result is ',t 
    yield t 
  
call = generator() 
next(call) 
next(call) 
next(call) 

Output :

First result is  1
Second result is  2
Third result is  3

Difference between Generator function and Normal function –

Once the function yields, the function is paused and the control is transferred to the caller.
When the function terminates, StopIteration is raised automatically on further calls.
Local variables and their states are remembered between successive calls.
Generator function contains one or more yield statement instead of return statement.
As the methods like _next_() and _iter_() are implemented automatically, we can iterate through the items using next().

There are various other expressions that can be simply coded similar to list comprehensions but instead of 
brackets we use parenthesis. These expressions are designed for situations where the generator is 
used right away by an enclosing function. Generator expression allows creating a generator without a yield keyword. 
However, it doesn’t share the whole power of generator created with a yield function. Example :

# Python code to illustrate generator expression  
generator = (num ** 2 for num in range(10))  
for num in generator: 
    print(num) 

Output :


0
1
4
9
16
25
36
49
64
81

We can also generate a list using generator expressions :

string = 'geek'
li = list(string[i] for i in range(len(string)-1, -1, -1)) 
print(li) 

Output:

['k', 'e', 'e', 'g']

There are two terms involved when we discuss generators.

Generator-Function : A generator-function is defined like a normal function, but whenever it needs to generate a value, 
it does so with the yield keyword rather than return. If the body of a def contains yield, 
the function automatically becomes a generator function.

# A generator function that yields 1 for first time, 
# 2 second time and 3 third time 
def simpleGeneratorFun(): 
    yield 1            
    yield 2            
    yield 3            
   
# Driver code to check above generator function 
for value in simpleGeneratorFun():  
    print(value) 

Output :

1
2
3

Generator-Object : Generator functions return a generator object. Generator objects are 
used either by calling the next method on the generator object or using the generator object 
in a “for in” loop (as shown in the above program).

# A Python program to demonstrate use of  
# generator object with next()  
  
# A generator function 
def simpleGeneratorFun(): 
    yield 1
    yield 2
    yield 3
   
# x is a generator object 
x = simpleGeneratorFun() 
  
# Iterating over the generator object using next 
print(x.__next__() ) # In Python 2, next() 
print(x.__next__() ) 
print(x.__next__() ) 

Output :

1
2
3

So a generator function returns an generator object that is iterable, i.e., can be used as an Iterators .


As another example, below is a generator for Fibonacci Numbers.
# A simple generator for Fibonacci Numbers 
def fib(limit): 
      
    # Initialize first two Fibonacci Numbers  
    a, b = 0, 1
  
    # One by one yield next Fibonacci Number 
    while a < limit: 
        yield a 
        a, b = b, a + b 
  
# Create a generator object 
x = fib(5) 
  
# Iterating over the generator object using next 
print(x.next()) # In Python 3, __next__() 
print(x.next()) 
print(x.next()) 
print(x.next()) 
print(x.next()) 
  
# Iterating over the generator object using for 
# in loop. 
print("\nUsing for in loop") 
for i in fib(5):  
    print(i) 

Output :

0
1
1
2
3

Using for in loop
0
1
1
2
3

Applications : Suppose we to create a stream of Fibonacci numbers, adopting the generator 
approach makes it trivial; we just have to call next(x) to get the next Fibonacci number 
without bothering about where or when the stream of numbers ends.
A more practical type of stream processing is handling large data files such as log files. 
Generators provide a space efficient method for such data processing as only parts of the file are 
handled at one given point in time. We can also use Iterators for these purposes, 
but Generator provides a quick way (We don’t need to write __next__ and __iter__ methods here).
