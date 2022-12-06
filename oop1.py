
===================|
Inheritance        |
===================|
class derived-classname(superclass-name) 


# A Python program to demonstrate working of inheritance 
class Pet: 
		#__init__ is an constructor in Python 
		def __init__(self, name, age):	 
				self.name = name 
				self.age = age 

# Class Cat inheriting from the class Pet 
class Cat(Pet):		 
		def __init__(self, name, age): 
				# calling the super-class function __init__ 
				# using the super() function 
				super().__init__(name, age) 

def Main(): 
		thePet = Pet("Pet", 1) 
		jess = Cat("Jess", 3) 
		
		# isinstance() function to check whether a class is 
		# inherited from another class 
		print("Is jess a cat? " +str(isinstance(jess, Cat))) 
		print("Is jess a pet? " +str(isinstance(jess, Pet))) 
		print("Is the pet a cat? "+str(isinstance(thePet, Cat))) 
		print("Is thePet a Pet? " +str(isinstance(thePet, Pet))) 
		print(jess.name) 

if __name__=='__main__': 
		Main() 



Output:
		Is jess a cat? True
		Is jess a pet? True
		Is the pet a cat? False
		Is thePet a Pet? True
		Jess


# A Python program to demonstrate inheritance 

# Base or Super class. Note object in bracket. 
# (Generally, object is made ancestor of all classes) 
# In Python 3.x "class Person" is 
# equivalent to "class Person(object)" 
class Person(object): 
	
	# Constructor 
	def __init__(self, name): 
		self.name = name 

	# To get name 
	def getName(self): 
		return self.name 

	# To check if this person is employee 
	def isEmployee(self): 
		return False


# Inherited or Sub class (Note Person in bracket) 
class Employee(Person): 

	# Here we return true 
	def isEmployee(self): 
		return True

# Driver code 
emp = Person("Geek1") # An Object of Person 
print(emp.getName(), emp.isEmployee()) 

emp = Employee("Geek2") # An Object of Employee 
print(emp.getName(), emp.isEmployee()) 

 Output:

		('Geek1', False)
		('Geek2', True)


# Python example to check if a class is 
# subclass of another 

class Base(object): 
	pass # Empty Class 

class Derived(Base): 
	pass # Empty Class 

# Driver Code 
print(issubclass(Derived, Base)) 
print(issubclass(Base, Derived)) 

d = Derived() 
b = Base() 

# b is not an instance of Derived 
print(isinstance(b, Derived)) 

# But d is an instance of Base 
print(isinstance(d, Base)) 


Output:

		True
		False
		False
		True


# Python example to show working of multiple 
# inheritance 
class Base1(object): 
	def __init__(self): 
		self.str1 = "Geek1"
		print("Base1")

class Base2(object): 
	def __init__(self): 
		self.str2 = "Geek2"		
		print("Base2")

class Derived(Base1, Base2): 
	def __init__(self): 
		
		# Calling constructors of Base1 
		# and Base2 classes 
		Base1.__init__(self) 
		Base2.__init__(self) 
		print("Derived")
		
	def printStrs(self): 
		print(self.str1, self.str2) 
		

ob = Derived() 
ob.printStrs() 

Output:

		Base1
		Base2
		Derived
		('Geek1', 'Geek2')


# Python example to show that base 
# class members can be accessed in 
# derived class using base class name 
class Base(object): 

	# Constructor 
	def __init__(self, x): 
		self.x = x	 

class Derived(Base): 

	# Constructor 
	def __init__(self, x, y): 
		Base.x = x 
		self.y = y 

	def printXY(self): 
	
	# print(self.x, self.y) will also work 
	print(Base.x, self.y) 


# Driver Code 
d = Derived(10, 20) 
d.printXY() 

Output:

		(10, 20)

# Python example to show that base 
# class members can be accessed in 
# derived class using super() 
class Base(object): 

	# Constructor 
	def __init__(self, x): 
		self.x = x	 

class Derived(Base): 

	# Constructor 
	def __init__(self, x, y): 
		
		''' In Python 3.x, "super().__init__(name)" 
			also works'''
		super(Derived, self).__init__(x) 
		self.y = y 

	def printXY(self): 

	# Note that Base.x won't work here 
	# because super() is used in constructor 
	print(self.x, self.y) 


# Driver Code 
d = Derived(10, 20) 
d.printXY() 

Output:

		(10, 20)


class X(object): 
	def __init__(self, a): 
		self.num = a 
	def doubleup(self): 
		self.num *= 2

class Y(X): 
	def __init__(self, a): 
		X.__init__(self, a) 
	def tripleup(self): 
		self.num *= 3

obj = Y(4) 
print(obj.num) 

obj.doubleup() 
print(obj.num) 

obj.tripleup() 
print(obj.num) 

Output:

		4
		8
		24

# Base or Super class 
class Person(object): 
	def __init__(self, name): 
		self.name = name 
		
	def getName(self): 
		return self.name 
	
	def isEmployee(self): 
		return False

# Inherited or Subclass (Note Person in bracket) 
class Employee(Person): 
	def __init__(self, name, eid): 

		''' In Python 3.0+, "super().__init__(name)" 
			also works'''
		super(Employee, self).__init__(name) 
		self.empID = eid 
		
	def isEmployee(self): 
		return True
		
	def getID(self): 
		return self.empID 

# Driver code 
emp = Employee("Geek1", "E101") 
print(emp.getName(), emp.isEmployee(), emp.getID()) 

Output:

		('Geek1', True, 'E101')



=================|
Iterators        |
=================|
Iterators are objects that can be iterated upon.

    Python uses the __iter__() method to return an iterator object of the class.
    The iterator object then uses the __next__() method to get the next item.
    for loops stops when StopIteration Exception is raised.


# This program will reverse the string that is passed 
# to it from the main function 
class Reverse: 
	def __init__(self, data): 
		self.data = data 
		self.index = len(data)		 

	def __iter__(self): 
		return self
	
	def __next__(self): 
		if self.index == 0: 
			raise StopIteration	 
		self.index-= 1
		return self.data[self.index] 

def Main(): 
	rev = Reverse('Drapsicle') 
	for char in rev: 
		print(char) 

if __name__=='__main__': 
	Main() 


Output :

		e
		l
		c
		i
		s
		p
		a
		r
		D

=================|
Generators       |
=================|
    Another way of creating iterators.
    Uses a function rather than a separate class
    Generates the background code for the next() and iter() methods
    Uses a special statement called yield which saves the state of the generator and 
    set a resume point for when next() is called again.


# A Python program to demonstrate working of Generators 
def Reverse(data): 
	# this is like counting from 100 to 1 by taking one(-1) 
	# step backward. 
	for index in range(len(data)-1, -1, -1): 
		yield data[index] 

def Main(): 
	rev = Reverse('Harssh') 
	for char in rev: 
		print(char) 
	data ='Harssh'
	print(list(data[i] for i in range(len(data)-1, -1, -1))) 

if __name__=="__main__": 
	Main() 


Output :

		h
		s
		s
		r
		a
		H
		['h', 's', 's', 'r', 'a', 'H']

# Python program to show that we can create 
# instance variables inside methods 

# Class for Computer Science Student 
class CSStudent: 
	
	# Class Variable 
	stream = 'cse'	
	
	# The init method or constructor 
	def __init__(self, roll): 
		
		# Instance Variable 
		self.roll = roll			 

	# Adds an instance variable 
	def setAddress(self, address): 
		self.address = address 
	
	# Retrieves instance variable	 
	def getAddress(self):	 
		return self.address 

# Driver Code 
a = CSStudent(101) 
a.setAddress("Noida, UP") 
print(a.getAddress()) 


class MyClass: 

	# Hidden member of MyClass 
	__hiddenVariable = 0
	
	# A member method that changes 
	# __hiddenVariable 
	def add(self, increment): 
		self.__hiddenVariable += increment 
		print (self.__hiddenVariable) 

# Driver code 
myObject = MyClass()	 
myObject.add(2) 
myObject.add(5) 

# This line causes error 
print (myObject.__hiddenVariable) 

Output :

		2
		7
		Traceback (most recent call last):
		  File "filename.py", line 13, in 
		    print (myObject.__hiddenVariable)
		AttributeError: MyClass instance has 
		no attribute '__hiddenVariable' 


# A Python program to demonstrate that hidden 
# members can be accessed outside a class 
class MyClass: 

	# Hidden member of MyClass 
	__hiddenVariable = 10

# Driver code 
myObject = MyClass()	 
print(myObject._MyClass__hiddenVariable) 

Output :

		10

Private methods are accessible outside their class, just not easily accessible. Nothing in Python is truly private; 
internally, the names of private methods and attributes are mangled and unmangled on 
the fly to make them seem inaccessible by their given names

class Test: 
	def __init__(self, a, b): 
		self.a = a 
		self.b = b 

	def __repr__(self): 
		return "Test a:%s b:%s" % (self.a, self.b) 

	def __str__(self): 
		return "From str method of Test: a is %s,""b is %s" % (self.a, self.b) 

# Driver Code		 
t = Test(1234, 5678) 
print(t) # This calls __str__() 
print([t]) # This calls __repr__() 

Output :

		From str method of Test: a is 1234,b is 5678
		[Test a:1234 b:5678]

If no __str__ method is defined, print t (or print str(t)) uses __repr__. 

class Test: 
	def __init__(self, a, b): 
		self.a = a 
		self.b = b 

	def __repr__(self): 
		return "Test a:%s b:%s" % (self.a, self.b) 

# Driver Code		 
t = Test(1234, 5678) 
print(t) 

Output :

		Test a:1234 b:5678

If no __repr__ method is defined then the default is used.

class Test: 
	def __init__(self, a, b): 
		self.a = a 
		self.b = b 

# Driver Code		 
t = Test(1234, 5678) 
print(t) 

Output :

		<__main__.Test instance at 0x7fa079da6710>