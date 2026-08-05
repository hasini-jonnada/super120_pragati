"""
print("pragati engineering college")
age = input("enter age")
print("my age is :"+age)


age = int(input())
print(f" my age is {age}")

#diff print statements
print('ideal\t computer \n institute')
print('vishnu '*3)
print('*' *7)

#concat of 2 str
str1 = "my name is "
str2 = "hasini"
print(str1+str2)

#variables list
a = 5
b = 6
c = 7
#print(a,b,c)

#variables with sep
print(a,b,c,sep = ',')
print(a)

#print strings in seperate lines
print('hello')
print('dear')
print('how are you')

#print join strings using space
print('hello',end = ' ')
print('dear',end = ' ')
print('how are you',end = ' ')

name = input("enter your name:")
print("hello "+ name)


#reverse a string
str = "hasini"
str1=""
print(str[::-1])

for i in range(len(str)-1,-1,-1):
    str1 += str[i]
print(str1)

str = "hasini"
str1 = ""
str1 = "".join(reversed(str))
print(str1)


#sum of 2 num
a = int(input("enter a value:"))
b = int(input("enter a value:"))
print(a+b)



#avg of 3 num
#n = int(input("enter no of val"))
a = int(input("enter val1:"))
b = int(input("enter val2:"))
c = int(input("enter val3:"))
avg = (a+b+c)//3
print(avg)



# area and peri 
r = int(input("enter radius:"))
print(f"area of circle: {3.14*r*r}")
n = int(input())
print(f"area of square: {4*n}")
l= int(input("enter len:"))
b = int(input("enter breadth:"))
area = l*b
print(f"area: {area}")
peri = 2*(l+b)
print("peri:",peri)


#employee details
empno= int(input("enter emp_no:"))
empname = (input("enter emp_name:"))
empsal = int(input("enter emp_sal:"))
dept = input("enter dept:")
address = input("enter adress:")
print("emp_no:",empno)
print("emp_name:",empname)
print("emp_sal:",empsal)
print("dept:",dept)
print("address:",address)


#arithmetic operations
a = int(input())
b = int(input())
print("a+b:",a+b)
print("a-b:",a-b)
print("a*b:",a*b)
print("a//b:",a//b)
print("a%b:",a%b)
print("a/b:",a/b)
print("a**b:",a**b)


#relational operator
a = int(input())
b = int(input())
print("a>b:",a>b)
print("a<b:",a<b)
print("a>=b:",a>=b)
print("a<=b:",a<=b)
print("a=b:",a==b)
print("a!=b:",a!=b)


#logical operators
a = int(input())
b = int(input())
print(a>b and a!=b)
print(a>b or a!=b)
print(not a<b)


#identity operators
a = int(input())
b = int(input())
print(a<b is a>b)
print((a<b) is not (a>b))
list1 =[1,2,3]
list2 =[1,2,3]
print((list1) is (list2))#false because stores in different memory
print(list1 is not list2)#true because stores in different memory
if a is 2:
    print(True)


#assignment operator
a = 3
b = 5
a+=b
print("a+=b:",a )
a-=b
print("a-=b:",a)
a*=b
print("a*=b:",a)
a//=b
print("a//=b:",a)
a%=b
print("a%=b:",a)
a/=b
print("a/=b:",a)
a**=b
print("a**=b:",a)


#operator precedence
print(10+8*6//5%4-5)
print((10+8)//(5*2%3))
print(10+(8//5*2)%3)

#type conv
a = 3
b = 2.5
print(type(a))
print(type(b))
c = a+b
print(type(c))
#type cast
c = int(a+b)
print(type(c))


#eligibility for vote
age = int(input())
if age >18:
    print("eligible for vote")
else:
    print("not eligible for vote")


#largest of 3
a = int(input())
b = int(input())
c = int(input())
if a>b and a>c:
    print("largest  element is",a)
elif b>c:
    print("the largest element is",b)
else:
    print("the largest element is",c)
    

#discount in mall
bill = int(input())
if bill >1000:
    discount = bill*0.1
else:
    discount = bill*0.01
final = bill-discount
print(final)


#vowels and consonents
ch = input()
if ch == 'a' or ch =='e' or ch =='i' or ch =='o' or ch =='u' or ch =='A' or ch =='E' or ch =='I' or ch =='O' or ch =='U' :
    print("vowels")
else:
    print("consonents")
    

#print days of week 
n = int(input())
if n == 1:
    print("monday")
elif n ==2:
    print("tuesday")
elif n == 3:
    print("wednesday")
elif n==4:
    print("thursday")
elif n == 5:
    print("friday")
elif n ==6:
    print("saturday")
elif n == 7:
    print("sunday")
else:
    print("invalid input and input must be in between 1 to 7")
    

# print seasons
mon = input()
if mon == "jan" or mon == "feb" or mon == "march" or mon == "april":
    print("winter season")
elif mon == "may" or mon == "june" or mon =="july" or mon== "aug":
    print("summer season")
elif mon == "sep" or mon == "oct" or mon == "nov" or mon =="dec":
    print("rainy season")
else:
    print("enter valid month")
    

#pos or neg and even or odd
n = int(input())
if n >0:
    if n %2 == 0:
        print("this is positve even number")
    else:
        print("this is positive odd number")
else:
    if n %2 == 0:
        print("this is negative even number")
    else:
        print("this is negative odd number")
        
 
#grades of subj
s1,s2,s3 = [int(x) for x in input().split(',') ]
if s1 >35 and s2>35 and s3>35:
    print("pass")
    t_sum = s1+s2+s3
    if t_sum >=90:
        avg = t_sum//3
    if avg >= 90:
        print("grade is A")
    elif avg >=80:
        print("grade is B")
    elif avg >= 70:
        print("garde is c")
    else:
        print("grade is D")
else:
    print("fail")
"""

#working with for loop
"""
for i in range(1,10):
    print(i)
for i in range(1,20,2):
    print(i)
for i in range(25,0,-1):
    print(i)
for i in range(0,25,-1):
    print(i)
for i in range(11):
    print("pragati engineering college")

    
max = int(input())
for i in range(0,max+1):
    print(i,end = " ")


#print the numbers between numbers
n1,n2 = [int(x) for x in input().split(',')]
print("the natural numbers between {} and {} are:".format(n1,n2))
for n in range(n1,n2+1):
    print(n)


#even numbers
if n1 %2 != 0:
    n1+=1
for n in range(n1,n2+1,2):
    print(n)
    


#armstrong number
n = int(input())
t =n 
res = 0
while t != 0:
    temp = t%10
    res += temp**3
    t //= 10
if res == n:
    print("yes")
else:
    print("no")
    

#strong number
def factorial(r):
    result = 1
    while r!= 0:
        result *= r
        r -= 1
    return result
    #recursive function for factorial
    #return n*factorial(n-1)
n = int(input())
t =n 
s = 0
while t!=0:
    r = t%10
    f = factorial(r)
    s +=f
    t //= 10
if s==n:
    print("yes ")
else:
    print("no")
    """
#strong numbers in between 1 to 2000
import math
def is_strong(n):
    t =n 
    s = 0
    while t!=0:
        r = t%10
        f = math.factorial(r)
        s +=f
        t //= 10
for i in range(0,2000):
    if is_strong(i):
        print(i)
    
"""
#perfect number
n = int(input())
sum = 0
for i in range(1,n):
    if n%i == 0:
        sum+=i
if sum == n:
    print("yes")
else:
    print("no")
   

#sum of digits
n = int(input())
sum = 0#123
while n!= 0:
    t = n%10
    sum += t
    n//=10
print(sum)


#reverse a number
n = int(input())
rev = 0
while n!=0:
    temp = n%10
    rev = rev*10 +temp
    n //=10
print(rev)


for i in range(5):
    print(i)
    if i == 3:
        break

for i in range(5):
    if i == 3:
        continue
    print(i)


num =5
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")
    split join find replace

     
str = "pRagaTi"
print(str.upper())
print(str.lower())
print(str.split())
print(str.replace("a","T"))
print(','.join(str))
print(str.find("a"))


#list slicing
nums = [2,3,5,6,7,8]
print(nums[::-3])
nums = [70,80,87,90,69]
print(nums[1:4])
nums =[1,6,3,4,8,9]
print(nums[::-2])
print(nums[-3::2])
print(nums[::-2])
print(nums[:2:-2])

#list methods
nums.append(98)
nums.insert(2,92)
nums.append(77)
print(nums)
print(max(nums))
print(min(nums))
print(nums.pop())
print(nums)
nums.remove(80)
print(nums)

nums = [3,50,4,1,10,5,9,20,50]
nums1 = [2,6]
print(nums.count(50))
nums.sort()
print(nums)
list = nums.copy()
print(list)
print(len(list))
nums.extend(nums1)
print(len(nums))
print(nums)
print(nums.clear())

nums = [2,4.5,'C',"urmila",True,10]
print('first = %d,last = %d'%(nums[0],nums[5]))
print('first = %c,last = %s'%(nums[2],nums[4]))
print('first = %f'%(nums[1]))

nums = []
for i in range(1,101,3):
    nums.append(i)
print(nums)

i =10
list =[]
while i <=19:
    list.append(i)
    i+=1
print(list)

list =[]
i=int(input())
count = 0
while count != 9:
    list.append(i)
    i+=1
    count+=1
print(list)

#nested lists
matrix =[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print(matrix[1])
print(matrix[1][2])
list =[2,'C',["abd",50],3.5]
print(list[2][1])


#tuples
tup =(1,6,3,4,8,9)
print(tup)
nested_tup = (1,(3,4),(6,2,9))
print(nested_tup[2][2])
my_tuple = (1,2.5,(True,False),'c',("abd","uma"))
print(my_tuple[2][1])

#sets
s1 ={3,6,8,1,9,8,20}
print(s1)
s1.remove(8)
print(s1)
s2 ={ 2,9,4,6,3,1}
print(s1.difference(s2))
print(s1.union(s2))
print(s1.intersection(s2))
print(s2.difference(s1))

print(s1|s2)
print(s1&s2)
print(s1-s2)
print(s2-s1)
print(s1^s2)#symmetric(remove all common elements)
s1 ={2,7,8,5,1}
s1.discard(7)
print(s1)


#dictionaries
dict ={"aa":1,"bb":2,"cc":3,"dd":4,"ee":5}
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict["aa"])
print(dict.get("aa"))
print(dict.get(1))

dict = {'sno':1,'name':"uma",'age':24}
print(dict)
dict["age"]= 21
dict["course"] ="python"
dict["address"]="kkd"
dict["fee"] = 4000
print(dict)
dict["course"]="java"
dict["fee"] = 50000
print(dict)
print(dict.pop("sno"))
print(dict)
print(dict.popitem())
print(dict)
print(dict.__delitem__("name"))
print(dict)
del dict["age"]
print(dict)
dict.clear()
print(dict)

dict = {'sno':1,'name':"uma",'age':24}
for i,j in dict.items():
    print("key:",i,",value:",j)
    print(f"key:{i},value:{j}")
for i,(key,value) in enumerate(dict.items()):
    print(f"index :{i},key:{key},value:{value}")

#tuples
tup1 =(1,2,3)
tup2=(4,5,6)
print(tup1+tup2)

x={}
max = int(input("how many students do you want"))
n = int(input("how many keys do you want"))
for s in range(max):
    for i in range(n):
        print("enter a key")
        k =input()
        print("enter a value")
        v = input()
        x.update({k:v})
    print(x)
    
dict = {'dict1':{'name':'uma','age':20,'course':'python'},
        'dict2':{'a':1,'b':2,'c':3,'d':[1,2]}}
print(dict['dict1'])
print(dict['dict2']['d'])
print(dict['dict1']['age'])

dict = {'dict1':{'name':'uma','age':20,'course':'python'},
        'dict2':{'name':1,'age':2,'course':3,'branch':4}}
print(dict['dict2']['name'])
print(dict['dict2'])


#functions
def add(a,b):
    sum =a+b
    print(sum)
add(10,20) 

def address():
    print("pragati college")
    print("adb road")
    print("surampalem")
    print("AP")
print("*"*70)
address()
print("*"*70)
address()
print("*"*70)

#function with para and with return values
def hello(str):
    return "hello"+str
str = hello("ram")
print(str)
str = hello("kiran")
print(str)

#function without para and with return values
def password():
    return "mani124"
pswd = password()
print(pswd)

#function without para and without return values
def add():
    a =10
    b =20
    sum =a+b
    print(sum)
add() 

#function with para and without return values
def hello(str):
    print("hello"+str)
str = hello("ram")
str = hello("kiran")

#default arguments
def greet(name = "student"):
    print("hello"+name)
greet()
greet("ramesh")


#class and object
class Car():
    s= "rolce Royce"
s1 = Car()
print(s1.s)



class names():
    a = "A"
    b = "B"
    c = "C"
    d = "D"
s1 = names()
s2 = names()
print(s1.a)
print(s1.b)
print(s2.c)
print(s2.d)



class Students:
    def __init__(self,name):
        self.name = name
    def display(self):
        print("Name:",self.name)
def greet():
    print("hello")
s1 = Students("uma")
s1.display()
greet()



class book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def display(self):
        print(f"book:{self.title},by:{self.author}")
b1 =book("how to speak in 2x","urmila")
b2 = book("panthulamma","navya")
b1.display()
b2.display()



class emp:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display(self):
        print("name:",self.name)
        print("salary:",self.salary)
class Myclass:
    @staticmethod
    def mymethod(e):
        e.salary+= 1000
        e.display()
e=emp("uma",50000)
e.display()
Myclass.mymethod(e)



class BankAccount:
    def __init__(self,acc_num,acc_holder,balance):
        self.acc_num = acc_num
        self.acc_holder = acc_holder
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print("deposited:",amount,"new balance:",self.balance)
    def withdraw(self,amount):
        if amount>= amount:
            self.balance -= amount
            print("withdrawl:",amount,"new balance:",self.balance)
    def checkBalance(self):
        print("current balance:",self.balance)
    def display(self):
        print("acc_num:",self.acc_num,"acc_holder:",self.acc_holder,"balance:",self.balance)
acc1 = BankAccount("12345","amit",5000)
acc2 = BankAccount("12344","arjun",6000)
acc1.display()
acc2.display()
acc1.deposit(5000)
acc1.withdraw(2000)
acc1.checkBalance()
acc2.deposit(5000)
acc2.withdraw(2000)
acc2.checkBalance()



class Example:
    a=15 
    b= 7
    def get(self,a,b):
        self.a = a
        self.b = b
    def show(self):
        print(f"a:{self.a} b:{self.b}")
    def cal(self):
        sum = self.a +self.b
        avg = sum/2
        print(f"sum:{sum} avg:{avg}")
e = Example()
e.get(10,20)
e.show()
e.cal()

a,b = [int(x) for x in input().split(',')]
e = Example()
e.get(a,b)
e.show()
e.cal()

e2 = Example()
e2.show()
e2.cal()


for i in range(3,7):
    if i!= 4:
        for j in range(1,11):
            print(f"{i}x{j} ={i*j}")
        print("\n")  
        

str = input()
print(str.upper())
print(str.count(" "))
print(str.replace(' ','_'))


class Vehicle:
    def __init__(self,brand,model,speed):
        self.brand = brand
        self.model = model
        self.speed = speed
        self.running = False
    def display(self):
        print(f" barnd:{self.brand},model:{self.model},speed:{self.speed}")
    def start(self):
        if self.running==False:
            self.running = True
        print(f"{self.brand} {self.model} started")
    def stop(self):
        if self.running == True:
            self.runniing = False
        print(f"{self.model} {self.model} stopped")
    def accelerate(self,increment):
        self.speed += increment
        print(f"{self.brand} {self.model} accelerate to {self.speed}")
car1 = Vehicle("toyota","corolla",60)
bike1 =Vehicle("honda","CBR",40)
car1.display()
bike1.display()
car1.start()
car1.accelerate(20)
car1.stop()

bike1.start()
bike1.accelerate(30)
bike1.stop()

#encapsulation
class Students:
    def __init__(self,name,marks):
        self.__name = name
        self.__marks = marks
    def display(self):
        print(f"name :{self.__name},marks:{self.__marks}")
s= Students("amit",90)
s.display()



class Student:
    def __init__(self,name,marks):
        self.__name = name
        self.__marks = marks
    def display(self):
        print(f"name :{self.__name},marks:{self.__marks}")
        

class Student:
    def __init__(self,name,marks):
        self.__name = name
        self.__marks = marks
    def get(self):
        return self.__marks
    def set(self,marks):
        if 0<=marks<=100:
            self.__marks = marks
        else:
            print("invalid marks")
    def display(self):
        print(f"Name :{self.__name},marks:{self.__marks}")
s =Student("neha",90)
s.display()
print("marks:",s.get())
s.set(95)
s.display()
s.set(110)
s=Student("amit",85)
s.display()


class Employee:
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,value):
        if value>0:
            self.__salary=value
        else:
            print("invalid salary")
    def display(self):
        print(f"employee:{self.__name},salary:{self.__salary}")
e = Employee("ravi",50000)
e.display()
print(e.salary)
e.salary =60000
e.display()
e.salary = -100 
"""

class OnlineShopping:
    def __init__(self,product_id,name,price,stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
    def update_stock(self,pieces):
        self.stock += pieces
        print(f"after update stock is {self.stock}")
    def apply_discount(self,percent):
        disc = self.price * (percent/100)
        self.price -= disc
        print(f"after discount the price is:{self.price}")
    def display(self):
        print(f"product_id:{self.product_id},name:{self.name},price :{self.price},stock:{self.stock}")
s = OnlineShopping(1,"amith",1000,30)
s.display()
s.update_stock(20)
s.apply_discount(10)

s1 = OnlineShopping(2,"arjun",2000,40)
s1.display()
s1.update_stock(45)
s1.apply_discount(10)
        