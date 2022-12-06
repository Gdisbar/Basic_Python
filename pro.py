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
