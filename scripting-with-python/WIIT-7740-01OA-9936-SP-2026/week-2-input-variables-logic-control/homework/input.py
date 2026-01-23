import sys

print("How would you like to calculate the circumference? Choose 'r' for radius or 'd' for diameter.")
circle_var = input()

if circle_var != 'r' and circle_var != 'd':
    print("Please enter either 'r' or 'd'.")
    sys.exit()
else:
    print("Please enter the length of your measurement.")
    length = int(input())

    if length <= 0:
        print("Please enter a number value greater than 0.")
        sys.exit()
    elif length > 0 and circle_var == 'r':
        r_circumference = 2 * length * 3.14159
        print(f"Using the length of {circle_var}{length}, the circumference of the circle is {r_circumference: .3f}.")
        sys.exit()
    else:
        d_circumference = length * 3.14159
        print(f"Using the length of {circle_var}{length}, the circumference of the circle is {d_circumference: .3f}.")
        sys.exit()
