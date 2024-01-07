# * How many sequences are there?
# * How many different subsequences are there and how many times each subsequence appears?
# * How many times each nucleotide appears in the whole file and how many errors are there? What is the frequency of each nucleotide and the errors?
# * The code should ask the user for the name of the file containing the sequences.

# filename = "given_text_file.txt" 
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} FILENAME   (name of DNA file)")
    exit()

#print(sys.argv)
# print(sys.argv[0])
# print(sys.argv[1])
# exit()

#filename = input("please give name of DNA file: ") 
filename = sys.argv[1]


def main():
    seq_counter=0
    subseq_counter=0
    unique_subseq_counter = {} #dictionary 

    total_letter_count = 0  


    nucleotide_counter = {} #dictionary 

    with open(filename) as fh:  # file handler
        # content = fh.readline() #read first line
        for line in fh:
            line = line.rstrip() #like=("\n")      
            # print(content, end="")
            # print(line)
            # line = ' '.join(line.split())

            sequences = line.split() #list of sequences
            # print(len(sequences))
            # print(sequences)

            number_of_seqs_in_current_line= len(sequences)
            # print(number_of_seqs_in_current_line)

            seq_counter += number_of_seqs_in_current_line

            for sequence in sequences:
                subsequences = sequence.split("X") #list of sequences
                # print(len(sequences))
                # print(subsequences)

                number_of_subseqs_in_current_sequence= len(subsequences)
                # print(number_of_seqs_in_current_line)

                subseq_counter += number_of_subseqs_in_current_sequence
                # print()

                for subsequence in subsequences: #for loop
                    # print(character)
                    if subsequence not in unique_subseq_counter:
                        unique_subseq_counter[subsequence] = 1
                    else:
                        unique_subseq_counter[subsequence] += 1

            letters = ["A", "C", "T", "G","X"] #list of strings
            for letter in letters: #for loop
                letter_count_in_line = line.count(letter)
                
                if letter not in nucleotide_counter:
                    nucleotide_counter[letter] = letter_count_in_line
                else:
                    nucleotide_counter[letter] += letter_count_in_line

                total_letter_count += letter_count_in_line  

            print()

    print(f"Total sequences {seq_counter}")
    # print(subseq_counter)
    print(f"Total unique sebsequences {unique_subseq_counter}")

    # print(nucleotide_counter)
    # print(counter["A"])
    print()
    print("Nucleotide & errors counts:")
    for letter in letters: 
        letter_count = nucleotide_counter[letter]
        letter_fraction = letter_count / total_letter_count
        print(f"{letter}: count: {letter_count}, fraction: {letter_fraction}")


main()
