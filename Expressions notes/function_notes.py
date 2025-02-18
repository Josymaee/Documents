# Joslynn Ramirez, Functio notes python

#functions hold actions to be reused
#number = int(input("please tell me a number:\n"))
#def add(numOne,numTwo):
#    print(numOne+numTwo)
    
#add(number,21)# Arguements set the value of the variable just for the instance of the functions
#add(8,12)
#add(6,4)
#print(numOne)

def values(type):
    return input(f"Please give me a {type}:\n")
name = values("name")
place = values("Place")
verb = values("verb")

print(f"{name} was really fast getting to {place} because they {verb} the whole way")