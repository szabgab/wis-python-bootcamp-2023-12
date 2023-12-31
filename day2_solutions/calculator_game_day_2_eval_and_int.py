import random

print("Lets play a game!")
print("But first, a little steup:)")
start_range = int(input("pick a number between 1-8:"))
end_range = int(input("pick a number between 2-10, and bigger from the last one:"))
number_of_attempts =int(input("pick one last number between 1-10:"))

print("Lets start the game!")

a = random.randrange(start_range, end_range)
b = random.randrange(start_range, end_range)

for _ in range(0, number_of_attempts):
    result = input(f"How much is ({a} + {b}) *({a}/{int(1)}))? ")
    if (a + b) * (a/int(1))== int(result):
        print(f"Indeed {result} is the correct number")
        break
    else:
        print("Incorrect")

print("now for the next game")
print("we have four basic mathematicl operators; +,-,/,*")
operators_list=[]
operators_list+=input("pick your favorite operator from the four:")
operators_list+=input("pick your next favorite operator from the four:")
operators_list+=input("now the thired in line from the four:")
operators_list+=input("and last one:")

for i in operators_list:
    result_2= input(f"How much is {a} {i} {int(1)}? ")
    for _ in range(0, number_of_attempts):
        if eval(f'{int(a)} {i} {int(1)}') == int(result_2):
            print(f"Indeed {result_2} is the correct number")
            break
        else:
            print("Incorrect")
print("Great job!")
