import random, threading

#Alphabet creation

chars = []

for x in xrange(65,91):
	chars.append(chr(x))
for x in xrange(97,123):
	chars.append(chr(x))

#Square creation

square = []
for x in xrange(100):
	square.append([]) 
	for y in xrange(100):
		square[x].append(random.sample(chars, 1))