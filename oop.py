class A:
	class_instance = 15

	def __init__(self,object_instance,time):
		self.object_instance = object_instance
		self.time = time

	def show(self):
		print(self.object_instance , self.time,self.class_instance)

	@classmethod	
	def print(cls):
		return cls.class_instance

	@staticmethod
	def info():
		return 'This is Static method'	

a=A("Raju",3)
a.show()
b=A("Raju",3)
b.time = 4
print("============================ modified class_instance ===============================")
b.show()
print('class_instance before updation ',A.class_instance)
A.class_instance = 23
print('class instance value updated %d'%A.class_instance)	
#A("test class A").display()
print('class method returns {}'.format(A.print()))
print('static method returns ===>',A.info())

print("================================= sub class =========================================")

class student:

	def __init__(self,name,roll):
		self.name = name
		self.roll = roll
		self.lap = self.laptop()

	def show(self):
		print(self.name,self.roll)	

	class laptop:
	
		def __init__(self):
			self.brand = 'ACER'
			self.ram = 12	

		def show(self):
			print(self.brand,self.ram)

s1=student('gorgio',29)
s1.show()
lap1 = s1.laptop()
lap1.ram = 8
lap1.show()	


print("============================ print last ==================================")
class printlast:
	def __init__(self):
		pass

	def inputfn(self):
		s1 = input('enter a string :: ')
		return s1

	def display(self,s1,s2=""):
	
		lis=s1.split(' ')
		for i in range(len(lis)):
			s2=s2+lis[i][-1]
		return s2

p=printlast()
inp = p.inputfn()
print(p.display(inp))

print("====================================== iterator ============================================")

class uptoten:

	def __init__(self):
		self.n = 1

	def __iter__(self):
		return self

	def __next__(self):
		if self.n <=5:
			val = self.n
			self.n += 1
			return val
		else:
			raise StopIteration

	

t = uptoten()
for i in t:
	print(i)			

print("=============== generator ===================================")

class A:
	def topeight(self):
		n=1
		while n<=8:
			yield n
			n+=1
#a=A()
c =A().topeight()
for i in c:
	print(i)			

print("================== iterator =================================")

a=[4,6,2,11,20,-7]

it = iter(a)

print(it.__next__())
print(it.__next__())

print("========== normal loop=========================================")
for i in a:
	print(i)
print("============== iterator loop(rest of the elements) ======================")	
for i in it:
	print(i)

print("======================= exception ========================================")

a = 5
b = 2
try:
	print("resource open")
	print(a/b)
	x = int(input("enter some no "))
	print(x)

except ZeroDivisionError as e:
	print("division by zero ",e)

except ValueError as e:
	print("type error ",e)		

except Exception as e:
	print("unknoen error ",e)

finally:
	print("resource closed")

print("============================================ polymorphism ========================")
print("==================== duck typing ================================")
class Dog:
	def talk(self):
		print("dog is barking")

class Cat:
	def talk(self):
		print("cat is mewing")

class Animal:
	def alive(self,species):
		species.talk()

d=Dog()
c=Cat()

live = Animal()			
live.alive(d)			
live.alive(c)

print("=============== operator overloading ============================")
a = 10
b = 58
print('using direct call ',int.__mul__(a,b))

class A:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __add__(self,other):
		x = self.x + other.x
		y = self.y + other.y
		z=A(x,y)
		return z

	def __mul__(self,other):
		x=self.x * other.x - self.y * other.y
		y=self.y * other.x + self.x * other.y
		zm=A(x,y)
		return zm

	def __gt__(self,other):
		x = self.x + self.y	
		y = other.x + other.y

		if x > y:
			return True
		else:
			return False	

	#def __str__(self):
	#	return ('{} ,{}'.format(self.x,self.y))		

a1=A(2,3)
a2=A(4,5)
a3 = a1 + a2
print('complex __add__ result : {}+{}j'.format(a3.x,a3.y))
a4 = a1 * a2
print('complex __mul__ result : {}+{}j'.format(a4.x,a4.y))		

if a1 > a2:
	print('a1 is grater ({} , {})'.format(a1.x,a2.y))
else:
	print('a2 is grater ({} , {})'.format(a2.x,a2.y))	
#print('without overloading',a1)
m =-553
print(m.__str__())
print('after overloading ',a1.__str__())	#uncomment __str__() to print values

print("======================== method overloading ===================================")

class N:
	def sum(self,a=None,b=None,c=None):
		if a!=None and b!=None and c!=None:
			return a+b+c
		elif a!=None and b!=None:
			return a+b	
		elif a!=None:
			return a
		else:
			return 0

n=N()
print(n.sum())
print(n.sum(1))				
print(n.sum(1,2))
print(n.sum(1,2,3))

print("======================== method overriding ===================================")

class B:
	def show(self):
		print("this is class B")
		
class C(B):
	pass
#	def show(self):
#		print("this is class C")

c = C()
c.show()	##uncomment show method of C

print("=============================== datatype ========================================")
print("======================== nested while loop ========================================================")
i = 1
while i<=3:
	print("1st while %d "%i)
	j=1
	while j<=2:
		print("2nd while %d "%j)
		j+=1
	i+=1	

for i in range(12,20,2):
	print(i)	

print("==================== prime within a range ========================================================")
a,b = [int(x) for x in input("enter the range ").split()]

for i in range(a,b):
	for j in range(2,i):
		if i%j==0:
			break;
	else:
		print(i)		

print("======================== taking multiple input ========================================================")
x=list(map(int,input("enter multiple value ").split()))
print(x)

print("======================== taking array input ========================================================")
from array import *
val = array('i',[int(k) for k in input().split()])
print()
newarr = array(val.typecode,(i*i for i in val))
for i in val:
	print(i,end=" ")
print()	

print("========================= inherite =================================================================")
class A():

	def __init__(self):
		print('class A constructor')

	def fun(self):
		print('class A ')

class B(A):

	def __init__(self):
		super().__init__()
		print('class B constructor')

	def fun2(self):
		print('class B')
			
class C():
	def fun(self):
		print('class C ')

class D(A,C):

	def __init__(self):
		super().__init__()		#method resolution order
		print('class C constructor')

	def fun4(self):
		print('class D ')	

	def fun(self):
		print('class A-D,race condition')		

class E(B):
	
	def __init__(self):
		super().fun2()	

print("B() :: ")	
b=B()			
print("b.fun() :: ")
b.fun()
print("b.fun2() :: ")
b.fun2()
print("D() :: ")
d=D()
print("d.fun() :: ") #biased towards fun of class A
d.fun()
print("d.fun4() :: ")
d.fun4()	
print("E() :: ")
e=E()
print("e.fun2() :: ")
e.fun2()
print("e.fun() :: ")
e.fun()


B() :: 
class A constructor
class B constructor
b.fun() :: 
class A 
b.fun2() :: 
class B
D() :: 
class A constructor
class C constructor
d.fun() :: 
class A-D,race condition
d.fun4() :: 
class D 
E() :: 
class B
e.fun2() :: 
class B
e.fun() :: 
class A 


print("============================= instance ========================================")
class FirstClass:
	def setdata(self,data):
		self.data = data

	def getdata(self):
		return self.data

class SecondClass(FirstClass):
	def __init__(self,data):
		self.data = data

	def __add__(self,other):
		return (self.data + other)

	def __str__(self):
		return ' %s' %self.data		
	

x = FirstClass()
x.setdata("python")
print('printing x %s'%x.getdata())

y = SecondClass('abc')
print('printing y %s'%y)
print(y.getdata())
z = y + 'xyz'
print('printing z  %s'%z)

'''
# cook your dish here
for _ in range(int(input())):
    k = 0
    for i in range(int(input())):
        id, s = map(int, input().split())
        k += (id - s)
    print(k)
'''

print("=============== multithread =============================================")
from threading import Thread
from time import sleep
class Hello(Thread):
	def run(self):
		for i in range(10):
			sleep(0.1)
			print("Hello")
		

class Hi(Thread):
	def run(self):
		for i in range(10):
			sleep(0.1)
			print("Hi")
			

t1=Hello()
t2=Hi()	

print("start")

t1.start()
sleep(0.05)
t2.start()	

t1.join()		#schedulers,
t2.join()

print("bye")

print("==================== function ======================================")
print("==================== returning multiple value from function ============================")
def add_mul(x,y):
	return x+y,x*y
m,n = add_mul(2,5)
print(m,n)	

print("==================== variable length args ================================================")
def num(*n):
	x = 0
	for i in n:
		x+=i
	print(x)
	
num(2,3,5,2)		

print("==================== variable length args(some args are defined) ==========================")
def id(name,**args):
	print(name)
	print(args)

id(name="Jotin",age=12,gender='M',visited=True)	

print("====================== return type is function ============================================")
def div(a,b):
	print(a/b)

def smart_div(func):

	def inner(a,b):
		if a<b:
			a,b=b,a
		return func(a,b)
	return inner

div1 = smart_div(div)
div1(2,4)			

print("=================== package ================================")
'''
file name : first.py
x = 9
def setx(n):
	global x
	x = n
	print(x)
'''
import first
#first.setx(8)

x = 11
def f1():
	x = 22
	print("inside f1 %d"%x)
	def f2():
		print("inside f2 %d"%x)
	return f2
var = f1()
var()

print("============== command ==========================")
import os
import subprocess
command = os.system("pwd")		#os.system('command') for single command on currect working directory
command2 = subprocess.call(['/bin/ls','-laS','/home/acroo/Music/'])  #subprocess.call('['/bin/ls','-laS','/home/acroo/Music/']') for 
																		#single command on any directory
command3 = os.popen("pwd").read()		#os.popen('command').read() to store command
print(command)
print(command2)
print(command3)

print("==================== Database ===========================================")
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="acroo",passwd="rasengun#19",database="student",auth_plugin="mysql_native_password")
mycursor = mydb.cursor()

#mycursor.execute("show databases")
mycursor.execute("select * from Student")
result = mycursor.fetchall()
for i in mycursor:
	print(i)

for i in result:
	print(i,end=" ")	
print()	

print("=============================== mutable default======================================")
from datetime import datetime
import time
def print_time(time_to_print=datetime.now()):
    print(time_to_print.strftime('%B %d, %Y %H:%M:%S'))

print(print_time.__defaults__)  

print_time()
time.sleep(1)
print_time()
time.sleep(1)
print_time()
time.sleep(1)
print_time()

def mod_print_time(time_to_print=None):
    if time_to_print is None:
        time_to_print = datetime.now()
    
    print(time_to_print.strftime('%B %d, %Y %H:%M:%S'))

print("========================= first class function ===============================")
def funA(msg):
    def funB():
        print('Hello : ',msg)

    return funB
    
f = funA("In f=funA() f is a function object(contains return value of funB) & it does'nt execute(funB()) until we put () i.e f()")
f()     

print("=====================================================================")
def html_tag(tag):
    def wrap_txt(msg):
        print('<{0}>{1}</{0}>'.format(tag,msg))
    return wrap_txt
    
p1=html_tag('h1')
print(p1)
p1('html msg 1')
#p1('html msg 2')       

print("====================================================================")
def outer():
    msg = 'outer fn object'
    def inner():
        print('after execution of inner() ===> return inner()')
        print(msg)

    return inner()

obj = outer()       

print("=====================================================================")

import logging
logging.basicConfig(filename='python_log.log',level=logging.INFO)

def logger(fun):
    def logger_fun(*args):
        logging.info('Running {} with args {}'.format(fun.__name__,args))
        print(fun(*args))
    return logger_fun
    
def add(x,y):
    return x+y  
def mul(x,y):
    return x*y


add_logger = logger(add)
add_logger(5,6)
mul_logger = logger(mul)
mul_logger(3,4)



print('=====================================================')
print(mod_print_time.__defaults__)  

mod_print_time()
time.sleep(1)
mod_print_time()
time.sleep(1)
mod_print_time()
time.sleep(1)
mod_print_time()
 

print("================ lambda expression=====================")
# Python code to illustrate 
# filter() with lambda() 
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(filter(lambda x: (x%2 != 0) , li)) 
print(final_list) 

# Python code to illustrate 
# map() with lambda() 
# to get double of a list. 
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(map(lambda x: x*2 , li)) 
print(final_list) 

# Python code to illustrate 
# reduce() with lambda() 
# to get sum of a list 
from functools import reduce
li = [5, 8, 10, 20, 50, 100] 
sum = reduce((lambda x, y: x + y), li) 
print (sum) 

# Function calling 
def dictionairy(): 

# Declaring hash function	 
key_value ={}	 

# Initializing the value 
key_value[2] = 56	
key_value[1] = 2
key_value[5] = 12
key_value[4] = 24
key_value[6] = 18	
key_value[3] = 323


print ("Task 3:-\nKeys and Values sorted", 
"in alphabetical order by the value") 

# Note that it will sort in lexicographical order 
# For mathematical way, change it to float 
print(sorted(key_value.items(), key =
			lambda kv:(kv[1], kv[0])))	 

def main(): 
	# function calling 
	dictionairy()			 
	
# main function calling 
if __name__=="__main__":	 
	main() 

# Python code to merge dict using update() method 
def Merge(dict1, dict2): 
	return(dict2.update(dict1)) 
	
# Driver code 
dict1 = {'a': 10, 'b': 8} 
dict2 = {'d': 6, 'c': 4} 

# This return None 
print(Merge(dict1, dict2)) 

# changes made in dict2 
print(dict2) 


# Python code to merge dict using a single 
# expression 
def Merge(dict1, dict2): 
	res = {**dict1, **dict2} 
	return res 
	
# Driver code 
dict1 = {'a': 10, 'b': 8} 
dict2 = {'d': 6, 'c': 4} 
dict3 = Merge(dict1, dict2) 
print(dict3) 

# Python program to illustrate 
# *args with first extra argument 
def myFun(arg1, *argv): 
	print ("First argument :", arg1) 
	for arg in argv: 
		print("Next argument through *argv :", arg) 

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks') 


# Python program to illustrate **kargs for 
# variable number of keyword arguments with 
# one extra argument. 

def myFun(arg1, **kwargs): 
	for key, value in kwargs.items(): 
		print ("%s == %s" %(key, value)) 

# Driver code 
myFun("Hi", first ='Geeks', mid ='for', last='Geeks')	 

def myFun(arg1, arg2, arg3): 
	print("arg1:", arg1) 
	print("arg2:", arg2) 
	print("arg3:", arg3) 
	
# Now we can use *args or **kwargs to 
# pass arguments to this function : 
args = ("Geeks", "for", "Geeks") 
myFun(*args) 

kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"} 
myFun(**kwargs) 
