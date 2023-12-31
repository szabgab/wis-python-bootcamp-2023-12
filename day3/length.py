filename = "sequence.txt"
#filename = input("filename (sequence.txt): ")

with open(filename) as fh:  # file handler
    sequence = fh.readline()

print("<{}>".format(sequence))
sequence = sequence.rstrip("\n")
print("<{}>".format(sequence))

print(len(sequence)) # function
number_of_a_letters = sequence.count("A") # method
print(number_of_a_letters)

number_of_c_letters = sequence.count("C")
print(number_of_c_letters)

number_of_t_letters = sequence.count("T")
print(number_of_t_letters)

number_of_g_letters = sequence.count("G")
print(number_of_g_letters)
