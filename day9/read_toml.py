import sys
import tomllib


def main():
    print(sys.argv)
    if len(sys.argv) < 2:
        exit(f"Usage: {sys.argv[0]} FILENAME")


    with open(sys.argv[1], 'rb') as fh:
        data = tomllib.load(fh)

    print(data)
    print(data["title"])
    print(data["database"]["ports"])
    print(data["database"]["ports"][0])


main()
