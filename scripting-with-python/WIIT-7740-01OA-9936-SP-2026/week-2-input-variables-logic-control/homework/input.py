import sys

print("How would you like to calculate the circumference? Choose 'r' for radius or 'd' for diameter.")
circle_var = input()

if circle_var != 'r' or circle_var != 'd':
    print("Please enter either 'r' or 'd'.")
    sys.exit()
else:
    print("Please enter the length of your measurement.")

