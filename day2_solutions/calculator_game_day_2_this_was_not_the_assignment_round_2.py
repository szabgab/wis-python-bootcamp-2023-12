#import random

#start_range = 1
#end = 50
#attempts = 3

print("Let's start the game!")

a = input('Give me a number from 1-10: a = ')
b = input('Give me another number from 1-10: b = ')
attempts = input('How many attempts do you want? ')

operators = input('Do you want to practice sums, multiplications or divisions? ')
if operators == 'sums':
    for times in range(0, int(attempts)):
        result = input(f'How much is {a} + {b}? ')
        if int(a) + int(b) == int(result):
            print(f'Indeed {result} is the correct number')
            print('done')
            break
        elif int(a) + int(b) > int(result):
            print(f'Higher!')
        else: 
            print(f'Lower!')
elif operators == 'multiplications':
    for times in range(0, int(attempts)):
        result = input(f'How much is {a} * {b}? ')
        if int(a) * int(b) == int(result):
            print(f'Indeed {result} is the correct number')
            print('done')
            break
        else: 
            print('Incorrect!')
elif operators == 'divisions':
    for times in range(0, int(attempts)):
        result = input(f'How much is {a} / {b}? ')
        if int(a) / int(b) == float(result):
            print(f'Indeed {result} is the correct number')
            print('done')
            break
        else: 
            print('Incorrect!')

