import json

name = input("Please, enter your name: ")
age = input("Please, enter your age: ")
favoriteFood = input("Please, enter your favorite food: ")

userData = {"Name": name, "Age": age, "Favorite Food": favoriteFood}
content = json.dumps(userData, indent=3)

print(content)
with open("output.json", "w") as file:
    file.write(content + "\n")
