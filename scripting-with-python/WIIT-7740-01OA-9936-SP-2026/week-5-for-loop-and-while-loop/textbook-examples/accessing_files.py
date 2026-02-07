from pathlib import Path

# retrieve .txt file from directory
path = Path('one-million.txt')

# read entire contents of .txt file
contents = path.read_text()

# break giant string into a LIST of individual strings (one for each line)
lines = contents.splitlines()

# initialize empty STRING
pi_string = ''

# for each line, perform string concatenation
for line in lines:
    pi_string += line.lstrip()

    # print a slice from 0 to 51st element in pi_string STRING
    # *We can perform indexing on strings*
    print(f"{pi_string[:52]}...")
    # print the length of pi_string
    print(len(pi_string))

'''
we can replace our FOR statement with the following: 
for line in contents.splitlines():  

this is more concise and we skip having to create the temporary 'lines' variable
'''
