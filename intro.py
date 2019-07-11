# Program by: Reginald Badua

print('Hello world!')
print("First PY program") # single or double quote
#variable, name and then value
name = "Reggie" #string
count = 9 #integer
found = False
average = 29.31 #floating point or double 

print(name)
# print variable types
# print(type(name))
# print(type(count))
# print(type(found))
# print(type(average))

print("***************")
print(10 + 10)
print (name + name)
print (name + str(count)) #parse a value
print("***************")
 
print(type(count))
number_string = str(count)
print(type(number_string))

print("***************")
provided = input('Please type your age: ')
print(type(provided))

increase = input('Please types another number:  ')
print(type(increase))

print('')
num1 = float(provided)
num2 = float(increase)
print(num1 + num2) #convert to integers to floats