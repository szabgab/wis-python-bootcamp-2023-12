filename = "characters.txt"

with open(filename) as fh:
    sequence = fh.readline()

sequence = sequence.rstrip("\n")

print(len(sequence))

counter = {}  # dictionary
for character in sequence:  # for loop
    #print(character)
    if character not in counter:
        counter[character] = 1
    else:
        # counter[character] = counter[character] + 1
        counter[character] += 1

print(counter)
# for character in counter.keys():
#     print(f"{character}: {counter[character]}")

# for character in sorted(counter.keys()):
#     print(f"{character}: {counter[character]}")

# for character in sorted(counter.keys(), key=lambda val: val.lower()):
#     print(f"{character}: {counter[character]}")

for character in sorted(counter.keys(), key=lambda val: counter[val], reverse=True):
    print(f"{character}: {counter[character]}")

