import random
print("Let's play a game!")
start = int(input ("Start at "))
end = int(input ("End at "))
attempts = int(input ("How many attempts do you want? "))
print("Choose an operation: +, -, /, *")
operation = input("Enter the operation you want to perform: ")
if operation not in ['+', '-', '/', '*']:
        print("Invalid operation selected!")
a = random.randrange(start,end)
b = random.randrange(start,end) 
for seq in range (0,attempts): 
    result = input(f"How much is {a} {operation} {b}?")
    if "+" in operation:
        if a + b == int(result):
            print (f"Indeed {result} is the correct number")
            break
        else: 
            print ("WRONG!!")
    if "-" in operation:
        if a - b == int(result):
            print (f"Indeed {result} is the correct number")
            break 
        else: 
             print ("WRONG!!")
    if "*" in operation:
        if a * b == int(result):
             print (f"Indeed {result} is the correct number")
             break 
        else: 
            print ("WRONG!!")
    if "/" in operation:
        if b != 0:  
            if a / b == round(float(result),3):
                print (f"Indeed {result} is the correct number")
                break 
            else: 
                 print ("WRONG!!")
    else:
        print ("Invalid Operation!")
print ("Done")
