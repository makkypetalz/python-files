# user_3_input=int(input('please enter your value'))
# num=2
# while num < user_3_input:
#     if user_3_input % num == 0:
#         print(f'{user_3_input} is not a prime number')
#         num=num + 1
#         print(num)
#     else:
#         print(f'{user_3_input} is a prime number')
#         break
# syntax is the arrangement of commands
# number = 0
# while number < 5:
#     print(number)
#     number = number + 1
# number = 0
# while number < 5:
#     print(number)
#     if number == 3:
#         break
#     number = number + 1

# number = 0
# while number < 5:
#     print(number)
#     if number == 6:
#         break
#     number = number + 1
# else:
#     print('no longer < 5')

# number = 0
# while number < 5:
#     number = number + 1
#     if number == 3:
#         continue
#     print(number)
# else:
#     print('no longer < 5')

# guess = int(input('guess a number between 1 and 100: '))
# number = 20
# while True:
#     if guess == number:
#         print('guess is correct')
#     elif guess > number:
#         print('guess too high')
#         break
#     else:
#         print('guess too low')
#         break
    
course = 'python'
for item in course:
    if item == 'o':
        continue
    print(item)
print('-------------')    
course = 'python'
for item in course:
    if item == 'o':
        break
    print(item)
    
for i in range(1, 100):
    if i % 2 == 1:
        print('it is a prime number')
    else:
        print('it is not a prime number')
        
    

    
    
    
    
    