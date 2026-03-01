file = './text/Harry_Potter.txt'
# open and read file
text = open(file, 'r')
read_text = text.read()

# split txt document at each period. will delete the periods in this process.
sentences = read_text.split('.')
for sentence in sentences:
    if 'Dursley' in sentence:
        print(sentence)