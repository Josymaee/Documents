#Joslynn Ramirez, Conditional notes Python
name = input("What is your name: \n")
#1. What puts something inside of the "if" statement
if name =="Ramirez":
    print("Hi Josy Ramirez")
# 2.What do if statement
    #checks a condition and if it is true it will do a thing
if name == "Ramirez": # <= this is the condition
    print("Hi Josy Ramirez") #<- This is what it does if true

#3. what are boolean statments?
#Part of your conditional that is either true or false
name = input("what is your first name: \n").strip().capitalize()
if name == "Josy": # Thi is the boolean statement <=
    print("Hello, Josy")
else:
    print(f"Hello, {name}!")

#4. what do else statments do?
#ends the condiotnal and
name = input("What is your first name?\n").strip().capitalize()
if name == "josy":
    print("Hello, josy")
else:
    print(f"Hello, {name}")

#5. What kind of statement do you use if you have more than 2 needed outcomes?
num = int(input("how many cookies are there?:\n"))
num = 2
if num == 0:
    print("There are none")
elif num == 1:
    print("There is one.")
elif num <4:
    print("There is a couple")
elif num <10:
    print("There are a few")
else:#else always ends the conditional
    print("There are many")

#6. What do each of the different symbols mean in conditionals? ,<,>, 
# < Less than
# > Graeter than
# <= Less than or equal to
# >= greater than or equal to
# == equal to (one = sets a variable)
# ===* Not in python
#! Not in

#7. What are 3 logical operators
elif num <10 and > 5: # and means both booleans must be true 
    print("This is a big single digit number")

elif num <10 or > 5: # or means one boolean must be true 
    print("This is a big single digit number")

elif not num < 10: #non of the balean statements can be true 
    print("this is a big single digit number")

#8. What are logical operators for?
#Allows the code to handle more difficult questions..increases complexity 

#9. What does a nested conditional statement do?
if num <10:
    if num ==8:
        print("This prints at 8") #nest as many conditionals as you want but past 3 its more confusing
    else:
        if num ==4:
        print("There are only enough cookies left for me. . . sorry")
    else:
        print("The number is less than 10")
else:
    print("The number is bigger than 10")

#10. What does the nested conditiona statamenst do?
if num <10: 
    if num ==8: