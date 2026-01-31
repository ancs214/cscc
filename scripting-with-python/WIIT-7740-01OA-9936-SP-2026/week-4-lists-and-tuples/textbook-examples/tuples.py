#tuples are similar to lists except we use parentheses and element values are immutable
dimensions = (200, 50, 11)
print(dimensions)

#we access them the same way we do lists
print(dimensions[0])
print(dimensions[1])

#if we try to change a value, we get an error
# dimensions[0] = 300
# print(dimensions[0])

#although you cannot modify, you can redefine the entire variable
rectangle_dimensions = (200, 50, 11)
print(rectangle_dimensions)
rectangle_dimensions = (300, 160, 2651)
print(rectangle_dimensions)

