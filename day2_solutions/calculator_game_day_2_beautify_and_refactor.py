import random

start_range=int(input("enter the starting range number:"))
end_range=int(input("entre the end of the range:"))
number_of_attempts=int(input("enter the number of attenpts:"))
opperator=input("what oppertaor woulf you like to test:")

print("Lets start the game!")

a = random.randrange(start_range, end_range)
b = random.randrange(start_range, end_range)

for _ in range(0, number_of_attempts):
    result = input(f"How much is {a} {opperator} {b}? ")
    if(opperator=="+"):
        if a + b == int(result):
            print(f"Indeed {result} is the correct number")
            break
        else:
            print("Incorrect")
    if(opperator=="-"):
        if a - b == int(result):
            print(f"Indeed {result} is the correct number")
            break
        else:
            print("Incorrect")
    if(opperator=="*"):
        if a * b == int(result):
            print(f"Indeed {result} is the correct number")
            break
        else:
            print("Incorrect")
    if(opperator=="/"):
        if a / b == float(result):
            print(f"Indeed {result} is the correct number")
            break
        else:
            print("Incorrect")

print("done")
