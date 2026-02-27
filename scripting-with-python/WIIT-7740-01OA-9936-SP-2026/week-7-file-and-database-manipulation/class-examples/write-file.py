file = './text/blankText.txt'
text = open(file, 'w')

for i in range(0, 11):
    text.write(str(i)+30*' ')
    text.write('\n')

text.write('The End')

# go to position 0, then write text at that position
text.seek(0)
text.write('The Start')

text.close()