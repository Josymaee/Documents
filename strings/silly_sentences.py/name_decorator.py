# Josy Ramirez, name decorator python

str_one = "Would you like your name in a different decoration"
str_two = "If yes, type your name again, if no you can leave the program"

# Welcoming the user
print("Hello! Thi is a program that makes your name look cool!.")

#Ask for name 
name = input("What is your name?\n").strip().upper()

print("==", name, "==")

name_2 = input("What is your name?\n").strip().upper()

print("(:(:", name_2, ":):)")

name_3 = input("What is your name?\n").strip().upper()

print("<<<", name_3, "<<<")

name_four= name.strip().capitalize()
print("Thank you for using my program, " + name_four + ":)")