
#input function
print('Enter your name:')
x = input()
print('Hello, ' + x)

#can also be written as:
x = input('Enter your name:')
print('Hello, ' + x)

#parrot program: example of using input
message = input('Tell me something, and I will repeat back to you: ')
print(message)

import sys

#while loops run as long as, or while, a certain condition is true
current_number = 1
while current_number <= 5:
    print(current_number)
    #x += y = x + x+y
    current_number += 1

#we can make a program run until the user says quit
prompt = '\nTell me something, and I will repeat it back to you:'
prompt += '\nEnter "quit" to end the program.'

message = ''
while message != 'quit':
    message = input(prompt)
    print(message)

#the above program still prints the word 'quit'
#we could instead use a flag to signal when to exit the loop
prompt = '\nTell me something, and I will repeat it back to you:'
prompt += '\nEnter "quit" to end the program.'
message = ''

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

#using break to exit a loop immediately without running any remaining code
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\nEnter 'quit' when you are finished."

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}")

#using continue to return to the beginning of the loop
#the program below will return odd numbers only
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)


