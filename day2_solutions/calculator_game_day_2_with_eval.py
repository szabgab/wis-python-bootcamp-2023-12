import random

start_range = int(input("Range start: "))
end_range = int(input("Range end: "))
number_of_attempts = int(input("number of attempts:"))

action = input("Desired mathematical action (+ OR - OR * OR /):")

print("Lets start the game!")

a = random.randrange(start_range, end_range)
b = random.randrange(start_range, end_range)

for _ in range(0, number_of_attempts):
    result = input(f"How much is {a} {action} {b}? ")
    if eval(f"{a}{action}{b}") == float(result):
        print(f"Indeed {result} is the correct number")
        break
    else:
        print("Incorrect")
