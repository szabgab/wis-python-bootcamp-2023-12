import random

start_range = 1
end_range = 20
number_of_attempts = 2

print("Lets start the game!")

a = random.randrange(start_range, end_range)
b = random.randrange(start_range, end_range)

for _ in range(0, number_of_attempts):
    result = input(f"How much is {a} + {b}? ")
    if a + b == int(result):
        print(f"Indeed {result} is the correct number")
        break
    else:
        print("Incorrect")


print("done")
