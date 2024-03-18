# class Staff:
#     def __init__(self, name, age, job):
#         self.name=name
#         self.age=age
#         self.job=job
#     def people(self):
#         return f'{self.name} is {self.age} years old, and is a {self.job}'

# f1=Staff('angela', 30, 'teacher')
# print(f1.people())

# class Student:
#     def __init__(self, name, age, location, country):
#         self.name=name
#         self.age=age
#         self.location=location
#         self.country=country
        
#     def female(self):
#         return f'{self.name} is {self.age} years old, she lives at {self.location} and shes from {self.country}'
    
#     def check(self):
#         if self.country == 'nigeria':
#            return f'{self.name} is given admission to study law'
#         else:
#            return 'dont'
       

# p1=student('sommy', 20, 'abuja', 'nigeria')
# print(p1.female())
# p2=student('chris', 23, 'florida', 'usa')
# print(p2.check())
# p3=student('babie', 25, 'kogi', 'nigeria')
# print(p3.check())

class Phones:
    def __init__(self, make, memory, storage, colour):
        self.make=make
        self.memory=memory
        self.storage=storage
        self.colour=colour
    
    def case(self):
        return f'{self.make} has {self.memory} and {self.storage} capacity with {self.colour} case'
        
f1=Phones('samsung', '4gb', 256, 'blue')
print(f1.case())
        
