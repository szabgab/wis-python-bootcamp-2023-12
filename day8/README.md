# Day 8

We started to go over the assignment submitted by Guy to read the code and make improvements

Default Dict: https://code-maven.com/slides/python/default-dict
https://docs.python.org/3/library/collections.html#collections.defaultdict


https://code-maven.com/slides/python/sorted

* It is better to use long and meaningful variable names
* better to have positive conditions
* better to return early from a function to reduce the load on the brain and to be able to outdent code.

* Suggested web site: https://exercism.org/

* openpyxl documentation: https://openpyxl.readthedocs.io/en/stable/tutorial.html
* source code: https://foss.heptapod.net/openpyxl/openpyxl
* openpyxl mapping column names and numbers: https://openpyxl.readthedocs.io/en/stable/api/openpyxl.utils.cell.html

dictionary comprehension 
top_institution = {key: institution[key] for key in top_institution if key in institution}



pandas
read_excel
df = read_csv(filename)

save_excel

df.columns
df.dtypes
df.index
df.values
df.describe()

df = pd.read_csv('mixed.csv', dtype = { 'MyInteger' : np.int8 })

df.head()
df.tail()
