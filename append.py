user_text = input("Please enter your name: ")

with open("output.txt", "w") as file:
    file.write(user_text + "\n")

print("Initial Text written in output.txt")

append_text = input("Please enter your name: ")

with open("output.txt", "a") as file:
    file.write(append_text + "\n")

print("additional Text written in output.txt")

print("Final Text written in output.txt")

with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())