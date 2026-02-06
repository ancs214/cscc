# Create a list
my_int_list = [25, 50, 100, 125, 200, 250, 500, ]
print("Integer list: ", my_int_list)

my_str_list = ['Michael','Richard','Alejandro','Robert']
print("String list: ", my_str_list)

my_float_list = [5.8, 4.6, 9.6]
print("Float list: ", my_float_list)

my_mix_list = [25, 'Richard', 5.8, 'Alejandro', 9.6, 125]
print("Mixed list: ", my_mix_list)

# Fetch 1st element of my_int_list
print("\nMy int list 1st element is: ", my_int_list[0])

# Fetch the last element of my_string_list
print("My string list last element is: ", my_str_list[3])
print("My string list last element using -1: ", my_str_list[-1])
print("My string list last element using len(): ", my_str_list[len(my_str_list)-1])

# Extend my_str_list with John, James, Harry
my_str_list.extend(['John', 'James', 'Harry'])
print("New extended list: ", my_str_list)

# Add the element 3.14  at index 2 of my_float_list
my_float_list.insert(2, 3.14)
print(my_float_list)

# Replace 2nd element with 7.2
my_float_list[1] = 7.2
print(my_float_list)

#Slice on my_str_list elements 2 to 5
print("Slice of string list, elements 2 through 4:", my_str_list[2:5])

# Iterate through my_int_list
for element in my_int_list:
    print(element)

# Check to see if a specific item exists in a list
if "Michael" not in my_mix_list:
    print('Michael does not exist in my_mix_list!')

# Print the length of my_int_list
print("Length of my_int_list is ", len(my_int_list))

# Print the sort list of my_float_list
#sort method vs sorted function: sorted creates a copy and sorts the copied list
my_float_list.sort()
print("Sorted list: ", my_float_list)

# Convert sorted list of my_"float_list to tuple
my_converted_float_list = tuple(my_float_list)
print("Converted list to tuple: ", my_converted_float_list)
