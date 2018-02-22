import sys, random, threading

def checkrow(word, square, row, found):
	for column in xrange(100-len(word)):
		if word == square[row][column]:
			found = True
			break
	return found

def checkcolumn(word, square, column, found):
	for row in xrange(100-len(word)):
		if word == square[row][column]:
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
		square[rows].append(random.sample(chars, 1))

#The actual wordsearch

output = ""

for i in xrange(len(dictionary)):
	found = False
	for x in xrange(100):
		t1 = threading.Thread(target=checkrow, args=(dictionary[i], square, x, found,))
		t2 = threading.Thread(target=checkcolumn, args=(dictionary[i], square, x, found,))
		if found == True:
			output += dictionary[i]
			break

#Printing the words of the square

print "The words that are in the square are:"
if output == "":
	print "No word was found"
else:
	for x in xrange(len(output)):
		print output[x]