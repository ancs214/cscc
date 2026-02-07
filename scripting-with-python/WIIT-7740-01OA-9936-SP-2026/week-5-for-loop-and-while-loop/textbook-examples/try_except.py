"""
show example of how to use try-except block for error handling
"""

print("Give me two numbers, and I will divide the first number by the second number.")
print("Enter 'q' to quit.")

while True:
    first_num = input('\nFirst number: ')
    if first_num == 'q':
        break

    second_num = input('\nSecond number: ')
    if second_num == 'q':
        break

    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)

