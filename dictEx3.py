# from sys import argv

print "enter the name of the file"
filename = raw_input()
txt = open(filename)
text = txt.read().replace(',', ' ').replace('.', ' ').replace('!', ' ')
words = text.split()

tally = {}
for word in words:
        count = tally.get(word, 0)
        count = count + 1
        tally[word] = count

for word, count in tally.item():
    print word, ':', count
