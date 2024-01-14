# Day 5

https://biopython.org/


https://en.wikipedia.org/wiki/FASTA_format
https://en.wikipedia.org/wiki/FASTQ_format

pip install biopython

HTTP Status codes: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
200 is fine


## Exit code (success == 0)
Linux macOS
 echo $?
 echo %ERROR_LEVEL%


https://biopython.org/wiki/SeqIO

https://biopython.org/wiki/SeqRecord


https://www.ncbi.nlm.nih.gov/nuccore/?term=Zea+mays+chloroplast

API

Slides related to the material: https://code-maven.com/slides/python/biology

## Assignment

* Write a program that will get a term on the command line and download N entries (also provided on the command line) from one of the databases supported by Entrez. In the comment of the code include your favorite search terms.
You can work with the nucleotide database, but I would love to see other databases.

```
download_sequence.py  SEARCH_TERM  N
```

* Write a program that will take a list of files in the format you decided to download. Read the sequences, show report of distribution of letters in each one of them.
Optional: If you have some more interesting statistic you can create, I'd happy to see that instead of mere distribution of the letters.

```
analyze.py  FILE FILE FILE ...
```

Save one ore more of the data files and write a test that will take those files and check if the results are as expected.

```
test_analyze.py
```


Put all the python and data files in the same folder called `day5` and upload that folder to Dropbox.

