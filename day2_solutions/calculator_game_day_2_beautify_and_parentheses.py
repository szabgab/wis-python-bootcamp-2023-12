import random
min= input(f"What is your lowest number? ")
max= input (f"What is your highest number? ")
trials= input (f"How many trials do you want? ")
operation= input(f"What calcul do you want? + - / x ? ")

start_range = int(min)
end_range = int (max)
number_of_attempts = int (trials)
ope= operation


a =  random. randrange (start_range, end_range)
b =  random. randrange (start_range, end_range)

for seq in range(0, number_of_attempts):

    if ope == ("+"):
        addition = input(f"how much is{a}+{b}?")
        if a + b == int(addition): 
            print(f"indeed {addition} is the correct number")
            break
        else:
            print("incorrect")
        
    else:
        if ope == ("-"):
            substraction = input(f"how much is{a}-{b}?")
            if a - b == int(substraction):
                print(f"indeed {substraction} is the correct number")
                break
            else:
                print("incorrect")
            
        else:
            if ope == ("/"):
                division = input(f"how much is{a}/{b}?")
                if a / b == int(division): 
                    print(f"indeed {division} is the correct number")
                    break
                else:
                    print("incorrect")
            else:
                if ope == ("x"):
                    multiplication = input(f"how much is{a}x{b}?")
                    if a * b == int(multiplication):
                        print(f"indeed {multiplication} is the correct number")
                        break
                    else:
                        print("incorrect")
print("done")
                    
    

                    


    
    



    
