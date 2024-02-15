import csv
import json

# csv file
with open("example1.csv", "r") as file:
    reader = csv.reader(file)

    try:
        for line in reader:
            print(line[0])
    except:
        print("Index ended!")

file.close()

# json file
with open("example2.json", "r") as file:
    data = json.load(file)
    out = json.dumps(data, indent=2)
    print(out)
file.close()
