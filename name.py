
print ('****Hello****') 
name = input('Please input your name: ')
print('Your name is:', name)

name_length = len(name) # get the length of a variable or array
print ("Your name has: ", name_length, "letters")
print ("The first letter is", name[0]) #read a character from the string
print ("In Uppers: ", name.upper()) #convert to uppercase
print(name.replace("R","X")) #replace S with X
contains = "X" in name # does the string contain an X [True or False]
print("Your name contains an X", contains)

print("****************************")
animal = input('What pet do you have? ')

# if statement
if ("CAT" in animal.upper()):
    print("So, its a cat")
elif ("DOG" in animal.upper()):
    print("So, its a dog")
else:
    print('Another type of animal')