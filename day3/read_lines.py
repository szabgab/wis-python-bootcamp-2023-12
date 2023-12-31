filename = "text.txt"

with open(filename) as fh:
    # content = fh.readline() # read first line
    for content in fh:
        content = content.rstrip()
        # print(content)
        #print(content, end="")
        #print(content, end="X")

# print(content)