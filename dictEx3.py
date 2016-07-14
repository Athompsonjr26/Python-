# from sys import argv

filename = raw_input('filename: ')
file = open(filename)
contents = file.read()
file.close()

contents = contents.replace('.', ' ')
words = contents.split()

tally = {}
for word in words:
        count = tally.get(word, 0)
        count = count + 1
        tally[word] = count

print tally
