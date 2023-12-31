import random

# probing the user inputs
start_range = input("what should be the smallest number? ")
end = input("what should be the highest number? ")
number_of_attempts = input("how many attempts do you need? ")
# Coded by the user's input = 1 to 4
operator = input("What will be the operator?\n 1 - addition\n 2 - substraction\n 3 - multiplication\n 4-division\n ")

start_range = int(start_range)
end = int(end)  + 1 # cause the function random.randrange dont take the upper range
number_of_attempts = int(number_of_attempts)
operator = int(operator)

# chosing the 2 numbers
a = random.randrange(start_range,end)
b = random.randrange(start_range,end)

# determining the operator and the result according to the user's choice
if operator == 1:
    operator = "+"
    result = a + b
elif operator == 2:
    operator = "-"
    result = a - b
elif operator == 3:
    operator = "*"
    result = a * b
elif operator == 4:
    operator = "/"
    result = a / b

# starting the game
print("Lets start the game")

for _ in range(0, number_of_attempts):
    result_user = input(f"how much is {a} {operator} {b}? ")
    if result == float(result_user):
        print(f"indeed {result_user} is the correct number")
        break
    else: 
        print("Incorrect")

print("done")
