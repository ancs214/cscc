"""
FILE_NAME: type-casting.py
AUTHOR: Ashley-Noel Swarn
DATE:
PURPOSE: To demo type casting
"""

number = 7
print(number)
print(type(number))
print(float(number))
print(type(float(number)))
print(str(number))
print(type(str(number)))

res = complex(number)
print(res)
print(type(res))


potato_salad_amount = 1.2
print("The amount of potato salad needed in liters is:", potato_salad_amount)
#versus
print('The amount of potato salad needed in liters is: ', potato_salad_amount)
#we do not need the space added after the colon; python automatically adds a space

