# Day 8


## Notes

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

```
top_institution = {key: institution[key] for key in top_institution if key in institution}
```


## pandas

```
read_excel
df = read_csv(filename)

save_excel
```

[numpy value types](https://code-maven.com/slides/python/value-types)

```
df.columns
df.dtypes
df.index
df.values
df.describe()

df = pd.read_csv('mixed.csv', dtype = { 'MyInteger' : np.int8 })

df.head()
df.tail()
```

[panda.Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html)

[ExcelWriter](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.ExcelWriter.html)

[PyPlot](https://matplotlib.org/stable/api/pyplot_summary.html)

## Videos


* Day 8 - part 1 https://youtu.be/JlDPIZ_eWZI
* Day 8 - part 2 https://youtu.be/Va5xYeWJIo0
* Day 8 - part 3 https://youtu.be/oweoPX6bEm4
* Day 8 - part 4 https://youtu.be/brtd61T4-TY


## Timestamps

First hour:
00:00 - reviewing last assignment
26:47 - using defaultdict
31:35 - exercism
34:25 - continue reviewing
37:53 - code comments
51:00 - writing informative
57:45 - constant

Second hour:
00:00 - reviewing last assignment
05:35 - sorting
16:30 - saving the results
25:15 - reviewing second code

Third hour:
00:00 - reviewing second code
16:30 - reading excel w\ pandas
31:30 - Numpy data types
38:48 - manipulating data frames

4th video:

00:00 - Sending Pull-Request to link to the project


