"""
FILE_NAME: magic-8-ball.py
AUTHOR: Ashley-Noel Swarn
DATE: 02-05-2026
PURPOSE: A program to emulate the magic 8 ball
"""

import random
import sys

messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy, try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

while True:
    #index the messages list to select a random element
    answer = messages[random.randint(0, len(messages) - 1)]

    print("\nWelcome to the Magic Eight Ball!")
    print("Please enter quit to exit.")
    question = input("Please submit your question to the Magic Eight Ball: ")

    if question == 'quit':
        sys.exit()

    print("The Magic Eight Ball says..." + answer)