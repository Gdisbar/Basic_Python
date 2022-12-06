Different types of iterators provided by this module are:


    Infinite iterators
    Combinatoric iterators
    Terminating iterators 

Infinite iterators

Iterator in Python is any Python type that can be used with a ‘for in loop’. Python lists, tuples, dictionaries, and sets are all examples of inbuilt iterators. But it is not necessary that an iterator object has to exhaust, sometimes it can be infinite. Such type of iterators are known as Infinite iterators.

Python provides three types of infinite itertors:

    count(start, step): This iterator starts printing from the “start” number and prints infinitely. If steps are mentioned, the numbers are skipped else step is 1 by default. See the below example for its use with for in loop.

    Example:

    # Python program to demonstrate  
    # infinite iterators  
        
    import itertools  
        
    # for in loop  
    for i in itertools.count(5, 5):  
        if i == 35:  
            break
        else:  
            print(i, end =" ") 

    Output:

    5 10 15 20 25 30

    cycle(iterable): This iterator prints all values in order from the passed container. It restarts printing from the beginning again when all elements are printed in a cyclic manner.

    Example 1:

    # Python program to demonstrate  
    # infinite iterators  
        
    import itertools  
        
    count = 0
        
    # for in loop  
    for i in itertools.cycle('AB'):  
        if count > 7:  
            break
        else:  
            print(i, end = " ")  
            count += 1

    Output:

    A B A B A B A B 

    Example 2: Using next function.

    # Python program to demonstrate  
    # infinite iterators  
        
    import itertools  
        
    l = ['Geeks', 'for', 'Geeks']  
        
    # defining iterator  
    iterators = itertools.cycle(l)  
        
    # for in loop  
    for i in range(6):  
            
        # Using next function  
        print(next(iterators), end = " ")  

    Combinatoric iterators
    Output:


    Geeks for Geeks Geeks for Geeks 

    repeat(val, num): This iterator repeatedly prints the passed value infinite number of times. If the optional keyword num is mentioned, then it repeatedly prints num number of times.

    Example:

    # Python code to demonstrate the working of    
    # repeat()   
          
    # importing "itertools" for iterator operations   
    import itertools   
          
    # using repeat() to repeatedly print number   
    print ("Printing the numbers repeatedly : ")   
    print (list(itertools.repeat(25, 4))) 

    Output:

    Printing the numbers repeatedly : 
    [25, 25, 25, 25]

Combinatoric iterators

The recursive generators that are used to simplify combinatorial constructs such as permutations, combinations, and Cartesian products are called combinatoric iterators.

In Python there are 4 combinatoric iterators:

    Product(): This tool computes the cartesian product of input iterables. 
    To compute the product of an iterable with itself, we use the optional repeat keyword 
    argument to specify the number of repetitions. The output of this function are tuples 
    in sorted order.

    Example:

    # import the product function from itertools module  
    from itertools import product  
        
    print("The cartesian product using repeat:")  
    print(list(product([1, 2], repeat = 2)))  
    print()  
        
    print("The cartesian product of the containers:")  
    print(list(product(['geeks', 'for', 'geeks'], '2')))  
    print()  
        
    print("The cartesian product of the containers:")  
    print(list(product('AB', [3, 4]))) 

    Output:

    The cartesian product using repeat:
    [(1, 1), (1, 2), (2, 1), (2, 2)]

    The cartesian product of the containers:
    [('geeks', '2'), ('for', '2'), ('geeks', '2')]

    The cartesian product of the containers:
    [('A', 3), ('A', 4), ('B', 3), ('B', 4)]

    Permutations(): Permutations() as the name speaks for itself is used to generate all possible permutations of an iterable. All elements are treated as unique based on their position and not their values. 
    This function takes an iterable and group_size, if the value of group_size is not specified or is equal to None then the value of group_size becomes length of the iterable.

    Example:

    # import the product function from itertools module  
    from itertools import permutations  
        
    print ("All the permutations of the given list is:")   
    print (list(permutations([1, 'geeks'], 2)))  
    print()  
      Terminating iterators 
    print ("All the permutations of the given string is:")   
    print (list(permutations('AB')))  
    print()  
        
    print ("All the permutations of the given container is:")   
    print(list(permutations(range(3), 2)))  

    Output:

    All the permutations of the given list is:
    [(1, 'geeks'), ('geeks', 1)]

    All the permutations of the given string is:
    [('A', 'B'), ('B', 'A')]

    All the permutations of the given container is:
    [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]

    Combinations(): This iterator prints all the possible combinations(without replacement) 
    of the container passed in arguments in the specified group size in sorted order.

    Example:

    # import combinations from itertools module  
        
    from itertools import combinations  
        
    print ("All the combination of list in sorted order(without replacement) is:")   
    print(list(combinations(['A', 2], 2)))  
    print()  
        
    print ("All the combination of string in sorted order(without replacement) is:")  
    print(list(combinations('AB', 2)))  
    print()  
        
    print ("All the combination of list in sorted order(without replacement) is:")  
    print(list(combinations(range(2), 1)))  

    Output:


    All the combination of list in sorted order(without replacement) is:
    [('A', 2)]

    All the combination of string in sorted order(without replacement) is:
    [('A', 'B')]

    All the combination of list in sorted order(without replacement) is:
    [(0, ), (1, )]

    Combinations_with_replacement(): This function returns a subsequence of length n from 
    the elements of the iterable where n is the argument that the function takes determining 
    the length of the subsequences generated by the function. Individual elements may repeat 
    itself in combinations_with_replacement function.

    Example:

    # import combinations from itertools module  
        
    from itertools import combinations_with_replacement  
        
    print ("All the combination of string in sorted order(with replacement) is:")  
    print(list(combinations_with_replacement("AB", 2)))  
    print()  
        
    print ("All the combination of list in sorted order(with replacement) is:")  
    print(list(combinations_with_replacement([1, 2], 2)))  
    print()  
        
    print ("All the combination of container in sorted order(with replacement) is:")  
    print(list(combinations_with_replacement(range(2), 1))) 

    Output:

    All the combination of string in sorted order(with replacement) is:
    [('A', 'A'), ('A', 'B'), ('B', 'B')]

    All the combination of list in sorted order(with replacement) is:
    [(1, 1), (1, 2), (2, 2)]

    All the combination of container in sorted order(with replacement) is:
    [(0, ), (1, )]Terminating iterators

Terminating iterators

Terminating iterators are used to work on the short input sequences and produce the output 
based on the functionality of the method used.

Different types of terminating iterators are:

    accumulate(iter, func): This iterator takes two arguments, iterable target and the 
    function which would be followed at each iteration of value in target. If no function is 
    passed, addition takes place by default. If the input iterable is empty, the output 
    iterable will also be empty.

    Example:

    # Python code to demonstrate the working of   
    # accumulate() 
      
      
    import itertools  
    import operator  
      
    # initializing list 1  
    li1 = [1, 4, 5, 7]  
        
    # using accumulate()  
    # prints the successive summation of elements  
    print ("The sum after each iteration is : ", end ="")  
    print (list(itertools.accumulate(li1)))  
        
    # using accumulate()  
    # prints the successive multiplication of elements  
    print ("The product after each iteration is : ", end ="")  
    print (list(itertools.accumulate(li1, operator.mul)))  
        
    # using accumulate()  
    # prints the successive summation of elements  
    print ("The sum after each iteration is : ", end ="")  
    print (list(itertools.accumulate(li1)))  
        
    # using accumulate()  
    # prints the successive multiplication of elements  
    print ("The product after each iteration is : ", end ="")  
    print (list(itertools.accumulate(li1, operator.mul)))  

    Output:

    The sum after each iteration is : [1, 5, 10, 17]
    The product after each iteration is : [1, 4, 20, 140]
    The sum after each iteration is : [1, 5, 10, 17]
    The product after each iteration is : [1, 4, 20, 140]

    chain(iter1, iter2..): This function is used to print all the values in iterable 
    targets one after another mentioned in its arguments.

    Example:

    # Python code to demonstrate the working of   
    # and chain()  
        
      
    import itertools 
      
    # initializing list 1  
    li1 = [1, 4, 5, 7]  
        
    # initializing list 2  
    li2 = [1, 6, 5, 9]  
        
    # initializing list 3  
    li3 = [8, 10, 5, 4] 
      
    # using chain() to print all elements of lists  
    print ("All values in mentioned chain are : ", end ="")  
    print (list(itertools.chain(li1, li2, li3)))  

    Output:

    All values in mentioned chain are : [1, 4, 5, 7, 1, 6, 5, 9, 8, 10, 5, 4]

    chain.from_iterable(): This function is implemented similarly as chain() but the 
    argument here is a list of lists or any other iterable container.

    Example:

    # Python code to demonstrate the working of   
    # chain.from_iterable() 
      
      
    import itertools 
      
      
    # initializing list 1  
    li1 = [1, 4, 5, 7]  
        
    # initializing list 2  
    li2 = [1, 6, 5, 9]  
        
    # initializing list 3  
    li3 = [8, 10, 5, 4]  
        
    # intializing list of list  
    li4 = [li1, li2, li3]  
      
    # using chain.from_iterable() to print all elements of lists  
    print ("All values in mentioned chain are : ", end ="")  
    print (list(itertools.chain.from_iterable(li4))) 

    Output:


    All values in mentioned chain are : [1, 4, 5, 7, 1, 6, 5, 9, 8, 10, 5, 4]

    compress(iter, selector): This iterator selectively picks the values to print from 
    the passed container according to the boolean list value passed as other arguments. 
    The arguments corresponding to boolean true are printed else all are skipped.

    Example:
    # Python code to demonstrate the working of   
    # and compress()  
      
      
    import itertools 
      
      
    # using compress() selectively print data values  
    print ("The compressed values in string are : ", end ="")  
    print (list(itertools.compress('GEEKSFORGEEKS', [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]))) 

    Output:

    The compressed values in string are : ['G', 'F', 'G']

    dropwhile(func, seq): This iterator starts printing the characters only after the func. 
    in argument returns false for the first time.

    Example:
    # Python code to demonstrate the working of   
    # dropwhile() 
      
      
    import itertools 
      
      
    # initializing list   
    li = [2, 4, 5, 7, 8]  
        
    # using dropwhile() to start displaying after condition is false  
    print ("The values after condition returns false : ", end ="")  
    print (list(itertools.dropwhile(lambda x : x % 2 == 0, li)))  

    Output:

    The values after condition returns false : [5, 7, 8]

    filterfalse(func, seq): As the name suggests, this iterator prints only values that 
    return false for the passed function.

    Example:

    # Python code to demonstrate the working of   
    # filterfalse()  
        
      
    import itertools  
        
    # initializing list   
    li = [2, 4, 5, 7, 8] 
      
    # using filterfalse() to print false values  
    print ("The values that return false to function are : ", end ="")  
    print (list(itertools.filterfalse(lambda x : x % 2 == 0, li)))  

    Output:

    The values that return false to function are : [5, 7]

    islice(iterable, start, stop, step): This iterator selectively prints the values 
    mentioned in its iterable container passed as argument. This iterator takes 4 arguments, 
    iterable container, starting pos., ending position and step.

    Example:

    # Python code to demonstrate the working of   
    # islice() 
        
       
    import itertools  
        
    # initializing list   
    li = [2, 4, 5, 7, 8, 10, 20]  
          
    # using islice() to slice the list acc. to need  
    # starts printing from 2nd index till 6th skipping 2  
    print ("The sliced list values are : ", end ="")  
    print (list(itertools.islice(li, 1, 6, 2)))  

    Output:

    The sliced list values are : [4, 7, 10]

    starmap(func., tuple list): This iterator takes a function and tuple list as argument 
    and returns the value according to the function from each tuple of list.

    Example:

    # Python code to demonstrate the working of   
    # starmap()  
        
      
    import itertools  
        
        
    # initializing tuple list  
    li = [ (1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10, 1) ]  
        
    # using starmap() for selection value acc. to function  
    # selects min of all tuple values
    print ("The values acc. to function are : ", end ="")  
    print (list(itertools.starmap(min, li)))  

    Output:

    The values acc. to function are : [1, 1, 4, 1]

    takewhile(func, iterable): This iterator is opposite of dropwhile(), it prints the 
    values till the function returns false for 1st time.

    Example:

    # Python code to demonstrate the working of   
    # takewhile() 
        
      
    import itertools  
        
    # initializing list   
    li = [2, 4, 6, 7, 8, 10, 20]  
        
    # using takewhile() to print values till condition is false.  
    print ("The list values till 1st false value are : ", end ="")  
    print (list(itertools.takewhile(lambda x : x % 2 == 0, li ))) 

    Output:

    The list values till 1st false value are : [2, 4, 6]

    tee(iterator, count):- This iterator splits the container into a number of iterators 
    mentioned in the argument.

    Example:

    # Python code to demonstrate the working of   
    # tee()  
        
      
    import itertools  
        
    # initializing list   
    li = [2, 4, 6, 7, 8, 10, 20]  
        
    # storing list in iterator  
    iti = iter(li)   
        
    # using tee() to make a list of iterators  
    # makes list of 3 iterators having same values.  
    it = itertools.tee(iti, 3)  
        
    # printing the values of iterators  
    print ("The iterators are : ")  
    for i in range (0, 3):  
        print (list(it[i]))  

    Output:

    The iterators are : 
    [2, 4, 6, 7, 8, 10, 20]
    [2, 4, 6, 7, 8, 10, 20]
    [2, 4, 6, 7, 8, 10, 20]

zip_longest( iterable1, iterable2, fillval): This iterator prints the values of iterables 
alternatively in sequence. If one of the iterables is printed fully, remaining values are 
filled by the values assigned to fillvalue.

# Python code to demonstrate the working of   
# zip_longest()  
    
  
import itertools  
    
# using zip_longest() to combine two iterables.  
print ("The combined values of iterables is  : ")  
print (*(itertools.zip_longest('GesoGes', 'ekfrek', fillvalue ='_' )))  

Output:

The combined values of iterables is  : 
('G', 'e') ('e', 'k') ('s', 'f') ('o', 'r') ('G', 'e') ('e', 'k') ('s', '_')

Iterable is an object, which one can iterate over. It generates an Iterator when passed to iter() method. 
Iterator is an object, which is used to iterate over an iterable object using __next__() method. 
Iterators have __next__() method, which returns the next item of the object.

Note that every iterator is also an iterable, but not every iterable is an iterator. For example, 
a list is iterable but a list is not an iterator. An iterator can be created from an iterable by 
using the function iter(). To make this possible, the class of an object needs either a method __iter__, 
which returns an iterator, or a __getitem__ method with sequential indexes starting with 0.

Code #1 :

for city in ["Berlin", "Vienna", "Zurich"]: 
    print(city) 
  
print("\n") 
      
for city in ("Python", "Perl", "Ruby"): 
    print(city) 
  
print("\n") 
      
for char in "Iteration is easy": 
    print(char, end = " ") 

Output :

Berlin
Vienna
Zurich

Python
Perl
Ruby

I t e r a t i o n   i s   e a s y 

 
When a for loop is executed, for statement calls iter() on the object, which it is supposed to loop over. 
If this call is successful, the iter call will return an iterator object that defines the method __next__(), 
which accesses elements of the object one at a time. The __next__() method will raise a StopIteration exception, 
if there are no further elements available. The for loop will terminate as soon as it catches a StopIteration exception.
 
Let’s call the __next__() method using the next() built-in function.


Code #2 : Function ‘iterable’ will return True, if the object ‘obj’ is an iterable and False otherwise.

# list of cities 
cities = ["Berlin", "Vienna", "Zurich"] 
  
# initialize the object 
iterator_obj = iter(cities) 
  
print(next(iterator_obj)) 
print(next(iterator_obj)) 
print(next(iterator_obj)) 

Output :

Berlin
Vienna
Zurich

Note: If ‘next(iterator_obj)’ is called one more time, it would return ‘StopIteration’.
 

Code #3 : Check object is iterable or not

# Function to check object 
# is iterable or not  
def iterable(obj): 
    try: 
        iter(obj) 
        return True
          
    except TypeError: 
        return False
  
# Driver Code      
for element in [34, [4, 5], (4, 5), 
             {"a":4}, "dfsdf", 4.5]: 
                   
    print(element, " is iterable : ", iterable(element)) 

Output :

34  is iterable :  False
[4, 5]  is iterable :  True
(4, 5)  is iterable :  True
{'a': 4}  is iterable :  True
dfsdf  is iterable :  True
4.5  is iterable :  False
