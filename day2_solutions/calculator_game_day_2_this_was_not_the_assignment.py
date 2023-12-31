import random

start_range = 1
end_range = 20
number_of_attempts = 3

print("Hello player! you need to pick 3 numbers and an operator, \nthen give me your anser for the calculation. You have 3 attempts! \nLets start the game!")

a = int(input("Pick the first number you would like to play with:"))
b = int(input("Pick the second number you would like to play with:"))
c = int(input("Pick the third number you would like to play with:"))
operator = input("Decide which operator you would like to play with (+/-/:/X):")

for i in range(0, number_of_attempts):
    player_answer = int(input(f"How much is {a} {operator} {b} {operator} {c}?"))
    if operator == "+":
        result = a + b + c
        if result == player_answer:
            print(f"Indeed {result} is the correct number!")
            break
        else:
            print("Incorrect")
            i += 1
    elif operator == ":":
        result = a / b / c
        if result == player_answer:
            print(f"Indeed {result} is the correct number!")
        else:
            print("Incorrect")
        break
    elif operator == "X":
        result = a * b * c
        if result == player_answer:
            print(f"Indeed {result} is the correct number!")
            break
        else:
            print("Incorrect")
            i += 1
    elif operator == "-":
        result = a - b - c   
        if result == player_answer:
            print(f"Indeed {result} is the correct number")
            break
        else:
            print("Incorrect")
            i += 1
print("Done!")
