class Fenwick:
    def __init__(self, n):
        sz = 1
        while sz <= n:
            sz *= 2
        self.size = sz
        self.data = [0] * sz

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i < self.size:
            self.data[i] += x
            i += i & -i

class Solution2(object):
    def processQueries(self, queries, n):
        fenw = Fenwick(2 * n)
        vimap = {}
        for i in range(1, n + 1):
            fenw.add(i + n, 1)
            vimap[i] = i + n
        cur = n
        #print(vimap)
        #print(fenw)
        ans = []
        for q in queries:
            i = vimap.pop(q)
            rank = fenw.sum(i-1)
            #print(f"{i} ----- {rank}")
            ans.append(rank)
            
            vimap[q] = cur
            fenw.add(i, -1)
            fenw.add(cur, 1)
            cur -= 1
        return ans


s = Solution2()
queries = [3,1,2,1]
#queries = [7,5,5,8,3]
#m = 8
m=5
print(s.processQueries(queries,m))




# class BIT:
#     """Implementation of a Binary Indexed Tree (Fennwick Tree)"""
    
#     #def __init__(self, list):
#     #    """Initialize BIT with list in O(n*log(n))"""
#     #    self.array = [0] * (len(list) + 1)
#     #    for idx, val in enumerate(list):
#     #        self.update(idx, val)

#     def __init__(self, list):
#         """"Initialize BIT with list in O(n)"""
#         self.array = [0] + list
#         for idx in range(1, len(self.array)):
#             idx2 = idx + (idx & -idx)
#             if idx2 < len(self.array):
#                 self.array[idx2] += self.array[idx]

#     def prefix_query(self, idx):
#         """Computes prefix sum of up to including the idx-th element"""
#         idx += 1
#         result = 0
#         while idx:
#             result += self.array[idx]
#             idx -= idx & -idx
#         return result

#     def range_query(self, from_idx, to_idx):
#         """Computes the range sum between two indices (both inclusive)"""
#         return self.prefix_query(to_idx) - self.prefix_query(from_idx - 1)

#     def update(self, idx, add):
#         """Add a value to the idx-th element"""
#         idx += 1
#         while idx < len(self.array):
#             self.array[idx] += add
#             idx += idx & -idx


# if __name__ == '__main__':
#     array = [1, 7, 3, 0, 5, 8, 3, 2, 6, 2, 1, 1, 4, 5]
#     bit = BIT(array)
#     print('Array: [{}]'.format(', '.join(map(str, array))))
#     print()

#     print('Prefix sum of first {} elements: {}'.format(13, bit.prefix_query(12)))
#     print('Prefix sum of first {} elements: {}'.format(7, bit.prefix_query(6)))
#     print('Range sum from pos {} to pos {}: {}'.format(1, 5, bit.range_query(1, 5)))
#     print()
    
#     bit.update(4, 2)
#     print('Add {} to element at pos {}'.format(2, 4))
#     new_array = [bit.range_query(idx, idx) for idx in range(len(array))]
#     print('Array: [{}]'.format(', '.join(map(str, new_array))))
#     print()

#     print('Prefix sum of first {} elements: {}'.format(13, bit.prefix_query(12)))
#     print('Prefix sum of first {} elements: {}'.format(7, bit.prefix_query(6)))
#     print('Range sum from pos {} to pos {}: {}'.format(1, 5, bit.range_query(1, 5)))
#     print()


class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


print(py_solution().int_to_Roman(1))
print(py_solution().int_to_Roman(4000))

print("==============================================================")

class find_sum:
    def find_sum_pair(self,lis,target):
        for i in range(0,len(lis)):
            for j in range(i+1,len(lis)):
                if lis[i]+lis[j] == target :
                    print('%d %d'%(lis[i],lis[j]))

    def remove_duplicate(self,lis,target):
        lis_new=[]
        for i in range(len(lis)):
            for j in range(i+1,len(lis)):
                if lis[i]==lis[j] and lis[i]!=target/2:
                    lis[j]=-999 
        lis_new=[lambda x:x>0,lis]
        return lis_new                          

lis=[10,20,10,40,50,60,70]
target = 20
x = find_sum()
lis_new = x.remove_duplicate(lis,target)
x.find_sum_pair(lis,target)



# def DAC_Max(a, l, r):
#     mx = -1
#
#     if (l >= r - 2):
#         if (a[l] > a[l + 1]):
#             return a[l]
#         else:
#             return a[l + 1]
#
#     # Logic to find the Maximum element
#     # in the given array.
#     mx = DAC_Max(a, l + 1, r)
#
#     if (a[l] > mx):
#         return a[l]
#     else:
#         return mx
#
#
# mn, mx = 0, -1
#
# # Initializing the array
# a = [70, 250, 50, 80, 140, 12, 14]
#
# # Recursion - DAC_Max function called
# print(DAC_Max(a, 0, 7))


def getTotalNumberOfSequences(m, n):
    # A special sequence cannot exist if length
    # n is more than the maximum value m.
    if m < n:
        return 0

    # If n is 0, found an empty special sequence
    if n == 0:
        return 1

    # There can be two possibilities : (1) Reduce
    # last element value (2) Consider last element
    # as m and reduce number of terms
    res = (getTotalNumberOfSequences(m - 1, n) + getTotalNumberOfSequences(m // 2, n - 1))

    return res

print(getTotalNumberOfSequences(10,4))


print("===============================================================")

# Algorithm:

# Declare a character stack S.
# Now traverse the expression string exp.
# If the current character is a starting bracket (‘(‘ or ‘{‘ or ‘[‘) then push it to stack.
# If the current character is a closing bracket (‘)’ or ‘}’ or ‘]’) then pop from stack and if the popped character is the matching starting bracket 
# then fine else parenthesis are not balanced.
# After complete traversal, if there is some starting bracket left in stack then “not balanced”

def areParanthesisBalanced(exp):
    s=[]
    for i in range(len(exp)):
        if exp[i]=='(' or exp[i]=='{' or exp[i]=='[':
            s.append(exp[i])
            continue
        #if current character is not opening parantheses then 
        #it must be closing so stack but can't empty at this point
        if len(s)==0:
            return False
        if exp[i]==')':
    
            x=s.pop()
            if x=='{' or x=='[':
                return False
        elif exp[i]=='}':
         
            x=s.pop()
            if x=='(' or x=='[':
                return False
        elif x==']':
            
            x=s.pop()
            if x=='(' or x=='{':
                return False      
    if len(s):
        return True
    return False

if __name__=='__main__':
    exp='({})[]'
    if areParanthesisBalanced(exp):
        print('vaild')
    else:
        print('invalid')      
    

print("========================= OOP ==========================================")
class Employee:

    def add_val(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def __repr__(self):
        return 'Name : {}, Age :{}, Salary : ${}k'.format(self.name,self.age,self.salary)

e1=Employee()
e2=Employee()
e3=Employee()       

e=[e1,e2,e3]
for i in range(len(e)):
    name = input('Name :')
    age=int(input('Age :'))
    salary=int(input('Salary :'))
    e[i].add_val(name,age,salary)

e_new = sorted(e,key=lambda e:e.age)

for emp in e_new:
    print(emp.__repr__())
#

def hello_decorator(func): 
    def inner1(*args, **kwargs): 
        
        print("before Execution") 
        
        # getting the returned value 
        returned_value = func(*args, **kwargs) 
        print("after Execution") 
        
        # returning the value to the original frame 
        return returned_value 
        
    return inner1 


# adding decorator to the function 
@hello_decorator
def sum_two_numbers(a, b): 
    print("Inside the function") 
    return a + b 

a, b = 1, 2

# getting the value through return of the function 
print("Sum =", sum_two_numbers(a, b)) 

