filename = "sequence.txt"
#filename = input("filename: ") # if I add an extra space when typing this will break the open

#print(f"filename: '{filename}'")
with open(filename) as fh:
    sequence = fh.readline()

print("<{}>".format(sequence))
sequence = sequence.rstrip("\n")
print("<{}>".format(sequence))

print(len(sequence))

letters = ["A", "C", "T", "G"]  # list of strings
# for letter in letters:  # for loop
#     # print(letter)
#     number_of_letters = sequence.count(letter)
#     #print(number_of_letters)
#     print(f"{letter}: {number_of_letters}")

counter = {}  # dictionary
for letter in letters:  # for loop
    number_of_letters = sequence.count(letter)
    counter[letter] = number_of_letters
    print(f"{letter}: {number_of_letters}")

print(counter)
# print(counter["A"])
for letter in letters:
    print(f"{letter}: {counter[letter]}")
