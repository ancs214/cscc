#input function
#print('Enter your name:')
#x = input()
#print('Hello, ' + x)


#can also be written as:
#x = input('Enter your name:')
#print('Hello, ' + x)


#or this way:
#message = input('Tell me something, and I will repeat back to you: ')
#print(message)

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






