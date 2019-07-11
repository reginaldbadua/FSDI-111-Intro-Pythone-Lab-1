# create an array

# add elements to an array
# animals.append("Lion")
# animals.append("Tiger")
# animals.append("Bear")

# print ("Animals in the array", len(animals))
# print(animals[0])

# # for loop over the array

# for animal in animals:
#     print(animal)

'''
Functionality:
    - present a recurring menu
    - exit the app with the x
    - allow the user to add animals to the array
    - allow the user to see the list of animals
'''
animals = []




def menu():
    print('\n\n\n\n')
    print("***Welcome to XYZ System***")
    print('-'*20)
    print('1 - Add new animal')
    print('2 - List the animals')
    print('3 - Count the animals')
    print('4 - Print the list in order(sorted alphabetically)')
    print('x - to close the system')
    opc = input ('Please choose an action: ')
    return opc

'''
Steps:
    - Ask input
    - append it to the array
'''
def create_new():
    new_animal = input('Animal name: ')
    animals.append(new_animal)
    print ('Animal saved!')
    input('Press enter to continue')

def print_list():
    for x in animals:
        print(x)

def count_list():
    print ("There are ", len(animals), "animals in the system")

def sorted_list():
    sorted_array = sorted(animals) # sort alphabetically
    for animal in sorted_array:
        print(animal)

# Start the app
selection = menu()
# print('You selected', selection)
while selection != 'x':
    selection = menu()
    
    if (selection == '1'):
        create_new()
    elif (selection == '2'):
        print_list()
    elif (selection == '3'):
        count_list()
    elif (selection == '4'):
        sorted_list()
    else:
        print('**Incorrect option, try again')
# this line outside the while loop
print ('Good bye')