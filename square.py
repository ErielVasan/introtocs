import sys, random

def checkrow(word, square, row, found):
	for column in xrange(100-len(word)):
		if word == square[row][column:column+len(word)]:
			found = True
			break
	return found


def checkcolumn(word, square, column, found):
	for row in xrange(100-len(word)):
		compare = ""
		for i in xrange(len(word)):
			compare += square[row + i][column] 
		if word == compare:
			found = True
			break
	return found

#Reading file

dictionary = ""
with open(sys.argv[1], "r") as f:
	dictionary = f.readlines()
f.close
dictionary = [x.strip() for x in dictionary]

#Alphabet creation

chars = []

for i in xrange(65,91):
	chars.append(chr(i))
for i in xrange(97,123):
	chars.append(chr(i))

#Square creation

square = []
for rows in xrange(100):
	square.append([]) 
	for columns in xrange(100):
		random.shuffle(chars)
		square[rows].append(chars[0])

#The actual wordsearch

output = []

for i in xrange(len(dictionary)):
	foundr = False
	foundc = False
	for x in xrange(100):
		foundr = checkrow(dictionary[i], square, x, foundr)
		foundc = checkcolumn(dictionary[i], square, x, foundc)
		if foundc == True or foundr == True:
			output.append(dictionary[i])
			break

#Printing the words of the square

print "The words that are in the square are:"
if output == "":
	print "No word was found"
else:
	pass
	print output
	for x in xrange(len(output)):
		print output[x]