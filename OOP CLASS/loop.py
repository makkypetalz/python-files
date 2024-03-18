# introduction to loop
# there two types of loop
# for loop are used for finite loop(loops you can count)
# while loop are used for both loops you can count and not count
'''
for variable condition iterable:
    output
'''

for i in range (20):
    print(i)
friends=['dera', 'john', 'gozie', 'buzor', 'ada', 'tochi']
for name in friends:
    print(name)
done=['good', 'good', 'good', 'bad', 'good', 'good', 'good', 'bad', 'good', 'good', 'good']
for item in done:
    if item =='bad':
        break
    print(item)
dude=['good', 'good', 'good', 'bad', 'good', 'good', 'good', 'bad', 'good', 'good', 'good']
for item in dude:
    if item == 'bad':
        continue
    print(item)
    student={
        'name':'makky',
        'age':20,
        'course':'geology',
        'fee':5000
}
for key in student:
    print(key.upper())
    
for key,value in student.items():
    print(f'{key.upper()}:{value}')
        
for i in range(20):
    print(i)
print('----------------------')
for i in range (2,7):
    print(i)
for i in range(5,30,10):
    print(i)
# 5 is start
# 30 is end or range
# 10 is step

courses=['html','css', 'js', 'python']
course_upper=[]
for course in courses:
    course_upper.append(course.upper())
print(course_upper)

list=[5,7,10,20,3,8]
n=0
for x in list:
    n+=x
print(n)

n=[]
for i in range (20):
    n.append(i)
print(n)
    
        
        


    

    