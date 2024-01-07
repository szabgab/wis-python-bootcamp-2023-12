file = input("enter file name:")
with open(file) as fh:
    total_sequences = 0
    total_subseq = 0
    subseq_counts = {}
    letter_counts = {}

    for line in fh:
        sequences = line.split()
        for seq in sequences:
            total_sequences += 1
            subsequences = seq.split("X")
            for subseq in subsequences:
                subseq = subseq.strip()
                total_subseq+= 1
                subseq_counts[subseq] = subseq_counts.get(subseq, 0) + 1
                for letter in subseq:
                    if letter in letter_counts:
                        letter_counts[letter] += 1
                    else:
                        letter_counts[letter] = 1
                if 'X' in letter_counts:
                    letter_counts['X'] += 1
                else:
                    letter_counts['X'] = 1

print("num of seq:", total_sequences)
print("num of subseq:", total_subseq)

print("\nsubseq Counts:")
for subseq, count in subseq_counts.items():
    print(f"subseq: {subseq}, count: {count}")

print("\nletter counts:")
for letter, count in letter_counts.items():
    print(f"letter: {letter}, count: {count}")
