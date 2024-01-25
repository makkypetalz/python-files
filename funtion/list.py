courses=['html', 'css', 'java', 'python']
print(list)
# list can collect any type of data
print(len(courses))
# list method
# append()add to the end of the list
courses.append('django')
print(courses)
courses.pop()
print(courses)
kep=courses.pop()
print(kep)
courses.insert(0, 'php')
print(courses)
courses.insert(3, 'lisp')
print(courses)

num1=[1, 2, 3, 4]
num2=[5, 6, 7, 8]
new_nums=num1+num2
print(new_nums)
print(num1*2)

# list slicing
friends=['jack', 'jerry', 'fred', 'friday', 'abdul']
print(friends[2:])
family=('john', 'jack', 'wendy', 'chichi')
# family.append()
print(family)
# list can be changed while tuple cannot be changed
new_family=list(family)
new_family.append('product')
family=tuple(new_family)
print(family)