# pip install pyyaml

from yaml import safe_load
import sys
import json

def main():
    print(sys.argv)
    if len(sys.argv) < 2:
        exit(f"Usage: {sys.argv[0]} FILENAME")


    with open(sys.argv[1]) as fh:
        data = safe_load(fh)
    print(data)
    print(data["versions"])
    print(data["versions"][0]["ladino"])

    with open("data.json", "w") as fh:
        json.dump(data, fh)

main()
