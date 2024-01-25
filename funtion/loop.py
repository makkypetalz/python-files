to_sort=[i for i in range(1,51) if i%2==1]
print(to_sort)

family=['chinwe', 'ugo', 'nneka', 'chuchu']
friends=['christian', 'gcee', 'freaky', 'teezy']
fans=['davido', 'wizkid', 'rema', 'joeboy']
name=input('please put your name')
if name in family:
    print(f'{name} am happy to have you as a family')
elif name in friends:
    print(f'{name} you are a wonderful friend')
elif name in fans:
    print(f'{name} thank you for your support')
else:
    print(f'{name} gutsetag?')

# break:this exits out of the loop so that no more iterations occurs
phones=['ok', 'ok', 'ok', 'ok', 'ok', 'bad', 'good', 'good', 'good', 'good', 'good', 'good']
for status in phones:
    if status=='bad':
        print('stop the production line')
        break
print(f'this phone is{status}')
# continue: it terminates the current
phones=['ok', 'ok', 'ok', 'ok', 'ok', 'bad', 'good', 'good', 'good', 'good', 'good', 'good']
for status in phones:
    if status=='bad':
        print('stop the production line')
        continue
    print(f'this phone is{status}')
# (start, range, end)

# for i in range(1,51,3)
    # print(i)
for i in range(2,15):   
    for x in range(2,i):
        if i%x==0: 
            print(f'{i} equals {x}*{i//x}')
            break
        else:
         print(f'{i} is a prime number')

students=[
    {'name':'christian', 'course': 'computer', 'grade': 56},
    {'name': 'john', 'course': 'english', 'grade': 66},
    {'name': 'great', 'course': 'economics', 'grade':76}
]

for student in students:
    name=student['name']
    course=student['course']
    grade=student['grade']
    print(grade)

   

#    while loop
# start
# while(condition)
# output
# increment/decrement

# i=0
# while(i<10):
#   print(i)
#   i+=1

# is_learning=true
# while is_learning:
#   print('we are learning)

while user_input=='yes'
    print('you are writing---')
    user_input=input('are you prepare to write the test?(yes/no):')
print('time-up')

friends=['christian', 'kennedy', 'bambo', 'john', 'teezy']
for counter, friend in enumerate(friends):
    print(counter,friend)
    
    # enumeration is used to count
    # zip:
fans=['davido', 'wizkid', 'rema', 'joeboy']
time_seen=[5,6,7,30,4]
long_seen={
    fans[i]:time_seen[i]
    for i in range(len(fans))
    if time_seen[i]>6
}
print(long_seen)


