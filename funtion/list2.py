courses=['accounting', 'html', 'python']
print(courses)
# # append is used to add to d end of the list 
courses.append('java')
print(courses)
courses.insert(3, 'lisp')
print(courses)
for i in courses:
    print(i.title())

    #  list slicing
friends=['jack', 'jerry', 'fred', 'friday', 'abdul']
print(friends)
print(friends[0:3])
print(friends[-4])
print(friends)

l1=[1,2,3,4,5,6]
l2=[7,8,9,10,11]
print(l1*3)
result=[]
print(result)

#  list comprehension
friends=['jack', 'jerry', 'fred', 'friday', 'abdul']
people[]
for i in friends:
people=[i.title() for i in friends]
print(people)

var=[i*5 for i in range(1,16)]
print(var)
list=['WENDY', 'CHUKS', 'UGO', 'CHICHI', 'charles', 'victor', 'prosper', 'coco', 'jerry', 'jack', 'john', 'james']
upper=[i for i in list if i == i.upper()]
print(upper)
lower=[i for i in list if i == i.lower()]
print(lower)
title=[i for i in list if i == i.title()]
print(title)