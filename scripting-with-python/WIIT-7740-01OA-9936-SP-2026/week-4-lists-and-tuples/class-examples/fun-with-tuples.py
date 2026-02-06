# Create a tuple
my_int_tuple = (25,50,75,100,125,200,250,500)
print(my_int_tuple)

my_str_tuple = ('hello', 'world', 'hola', 'mundo')
print(my_str_tuple)

my_float_tuple = (1.1, 2.2, 3.3, 4.4, 5.5, 6.6)
print(my_float_tuple)

my_mix_tuple = (25, 'Richard', 5.8, 'Alejandro', 9.6, 125)
print(my_mix_tuple)

for element in my_str_tuple :
    print(element)

concatenated = my_str_tuple + my_int_tuple
print(concatenated)

# Print out length of my_str_tuple
print("Length of my string tuple is ", len(my_str_tuple))

# convert the my_mix_tuple to a list
my_converted_mix_tuple = list(my_mix_tuple)
print("Converted tuple to a list: ", my_converted_mix_tuple)


