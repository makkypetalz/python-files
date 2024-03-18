# numb=[1, 2, 3, 4, 5, 6]
# del numb[2]
# print(numb)
# del numb[-2]
# print(numb)
# name=input('please enter your name')
# age=int(input('please enter your age'))
# if age >=9 and age <=11:
#     print('green house is too young to play')
# elif age >=12 and age <=14:
#     print('yellow house')
# elif age >=15 and age <=17:
#     print('red house')
# elif age >=18 and age <=19:
#     print('blue house')
# else:
#     print('you are too old to play')
    
n=[]
for i in range(1,20):
    if i%2==0:
        n.append(i)
print(n)

for i in range(1,102):
    if i %3 ==0:
        print('wuse')
    elif i % 5==0:
        print('abuja')
    elif i %3==0 and i % 5==0:
        print('wuse in abuja')    
    else:
        print(i)
        
# class Pet:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#     def show(self):
#         print(f" i am {self.name} and i am {self.age} years old")
# class Cat(Pet):
#     def speak(self):
#         print('meow')
        
# class Dog(Pet):
#     def speak(self):
#         print('bark')
        
# p=Pet('tim', 19)
# p.show()
# s=Cat('yul', 20)
# s.show()
# s.speak()
# d=Dog('moon', 30)
# d.show()
# d.speak()

# class Person:
#     number_of_people = 0
    
#     def __init__(self, name):
#         self.name=name
#         number_of_people = 8
        
        
# # p1 = Person('tim')
# # p2 = Person('jill')
# print

def my_function(fname):
    print(fname + "ref")
my_function("toby")
my_function("richy")
my_function("charles")

def my_function(fname, iname):
    print(fname + "" + iname)
my_function("emil","male")

def school(item, cloth, wear):
    print(f"I need {item},{cloth} and {wear} for school")
school("bag", "uniform", "shoe")

def children(*kids):
    print(f"Their names are " + kids[4])
children("muna","joy","buzor","chioma","josh")

def kids(child3,child2,child1):
    print(f"The Children are " + child3)
kids(child1="mary",child2="naza",child3="dera")

def money(naira):
    print(f"The boy loves {naira}")
money(20)

def family(child3,child2,child1):
    print(f"The eldest is {child2}, younger is {child3}, then the youngest is {child1}")
family("dera","muna","mercy")

def child(**kid):
    print("the boys name is " + kid["name"])
child(fname="emy", name="fiona")

def location(country="norway"):
    print("i am from " + country)
location("sweden")
location("america")
location()
location("atlanta")

def item(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
item(fruits)

def number(x):
    return 5*x
print(number(3))
print(number(5))
print(number(2))
    
# def tri_recursion(k):
#     if (k>0):
#         result = k + tri_recursion (k-1)
#         print(result)
#     else:
#         result = 0
#         return result
# print("recursion is done") 
# tri_recursion(7)
y = lambda x,z:x*z
print(y(5,2))
x = lambda m,y,n:m+y+n
print(x(5,4,3))
print((lambda x,y:x+y)(4,4))

def my_func(n):
    return lambda a:a*n
money = my_func(2)
print(money(5))
      
        