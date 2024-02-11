#import openpyxl
def process(filename):
    print(filename)
    #wb = openpyxl.load_workbook(filename)

    with open(filename) as fh:
        number = fh.readline()
    print(number)
    # if int(number) == 0:
    #     print("Cannot divide by zero")
    #     return
    
    result = 100 / int(number)
    print(result)
