import sys
# pip install requests
import requests

def main():
    print(sys.argv)
    if len(sys.argv) < 2:
        exit(f"Usage: {sys.argv[0]} API_FILE LOCATION")


    filename = sys.argv[1]
    location = sys.argv[2]

    with open(filename) as fh:
        api_key = fh.readline().rstrip()

    api_key = "e6449256b0ea85b78f044f45fd1a145d"
    print(api_key)


    url = "https://api.openweathermap.org/data/3.0/weather?q={}&units=metric&appid={}".format(location, api_key)
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    print(data)

main()