from Bio import Entrez
Entrez.email = "gabor@szabgab.com"

term = "Zea mays chloroplast"

# handle = Entrez.esearch(db="nucleotide", term=term, idtype="acc", retmax=30)
# record = Entrez.read(handle)
# #print(record)
# print(record["Count"])
# print(record["IdList"])
# print(len(record["IdList"]))
# handle.close()

doc_id = "CP120461.1"
handle = Entrez.efetch(db="nucleotide", id=doc_id, rettype="fasta", retmode="text")
data = handle.read()
handle.close()

print(data)