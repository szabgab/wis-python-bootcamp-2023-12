from Bio.Seq import Seq 
from Bio import SeqIO
import requests



# seq = "AGTC"

#my_seq = Seq("AGTCXCU")
# print(my_seq)
# print(my_seq.complement())

url = "https://raw.githubusercontent.com/biopython/biopython/master/Doc/examples/ls_orchid.fasta"
filename = "ls_orchid.fasta"
file_type = "fasta"

# result = requests.get(url)
# #print(result.status_code)
# if result.status_code != 200:
#     print("something went wrong")
#     exit(1)

# #print("success")
# #print(result.text)
    
# with open(filename, 'w') as fh:
#     fh.write(result.text)

print(SeqIO.parse(filename, file_type))

for seq_record in SeqIO.parse(filename, file_type):
    #print(seq_record)
    #print(seq_record.id)
    #print("--")
    #print(seq_record.description)
    print(seq_record.seq)
    print("--")
    print(seq_record.seq.complement())
    print("--------------")
    
