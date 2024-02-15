file = open("user_info.txt", "a")
name = input("Please, enter your full name: ")
file.write(name + "\n")
file.close
