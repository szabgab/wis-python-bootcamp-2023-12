import random


while True:
 start_range= int(input("choose a number from 1 to 20:"))
 end_range=int(input(f"choose a number from {start_range+1} to 20:"))
 if start_range<0 or start_range>20 or end_range<(start_range+1) or end_range>20:
   print("restart")
   continue
 else:
  break
 
a= random.randrange(start_range,end_range)
b= random.randrange(start_range,end_range)
   
#choose number of attempts
number_of_attempts =int(input("how many attempts do you want?"))
# choose math operator
math_operator=input("Enter calculation symbols for calculation you want to perform: ")


print("lets start the game")

for _ in range(0, number_of_attempts): 
  print(f"how much is {a} {math_operator} {b}?")
  result = float(input())
  if ((float(a + b) == result and math_operator == '+') or (float(a - b) == result and math_operator == '-') or (float(a * b) == result and math_operator == '*') or (round (a / b) == round(result) and math_operator=='/')):
    print (f" {int(result)} is correct")
    break
  else:
    print ("incorrect")


print("done")
