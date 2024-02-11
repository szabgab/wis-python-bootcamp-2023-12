import sys
from mylib import process

def main():
    print(sys.argv)
    print(sys.argv[1:])
    for filename in sys.argv[1:]:
        try:
            process(filename)
        except FileNotFoundError:
            print(f"File not found - Could not process '{filename}'")
            # break
        except ZeroDivisionError:
            print(f"Cannot divide by zero  - Could not process '{filename}'")
            
        # except Exception as err:
        #     print(f"There was an exception '{err}' - Could not process '{filename}'")

        # except (FileNotFoundError, ZeroDivisionError):
        #     print("error")


main()