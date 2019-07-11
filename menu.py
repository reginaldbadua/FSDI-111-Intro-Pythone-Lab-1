print('Welcom to myCalc')

num1 = input('Please type a number:  ')
num2 = input('Please type another number:  ')

# parse a string to floats
float1 = float(num1)
float2 = float(num2)

# math operations
print("Sum: ", float1 + float2)
print("Sub:  ", float1 - float2)
print("Mul:  ", float1 * float2)
print("Div:  ", float1 / float2)
print("Div:  ", float1 // float2)
print("Div:  ", float1 % float2)

#define a function
def say_hello():
    print('Hello from a function') #indentation

def perform_sum(num1, num2):
    float2 = 20
    other_stuff = "asdasdasd"
    print(num1 + num2)
    res = num1 + num2
    print(res)
    return res # return the result from the function, variable only exist inside the scope

# print ('im outside the function')

#exec (call) the function
say_hello()
print(num1)
result = perform_sum(float1,float2) # catch the return from a function
print('Result from functon', result)


# firstName (camel case)
# first_name 