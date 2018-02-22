import sys

#reading file. 

f = open(sys.argv[1], "r")
code = f.read() #Assigning the contents of the file to one string
f.close

#Empty file check

if code == "":
	print "Error! File is empty!"
	sys.exit

codePosition = 0
registry = [0]
registryPosition = 0

#Code Execution

while codePosition < len(code):

	if code[codePosition] == ">": #Move the pointer to the right
		registryPosition += 1
		if len(registry) <= registryPosition:
			registry.append(0)
		if registryPosition > 30000: #Registry overflow check
			print "Error! Registry overflow!"
			sys.exit
	
	elif code[codePosition] == "<": #Move the pointer to the left
		registryPosition -= 1
		if registryPosition < 0: #Registry underflow check
			print "Error! Registry underflow!"
			sys.exit

	elif code[codePosition] == "+": #Increment the memory cell under the pointer
		registry[registryPosition] += 1
		if registry[registryPosition] > 255: #Byte overflow, returns to 0
			registry[registryPosition] = 0

	elif code[codePosition] == "-": #Decrement the memory cell under the pointer
		registry[registryPosition] -= 1
		if registry[registryPosition] < 0: #Byte undeflow returns to 255
			registry[registryPosition] = 255

	elif code[codePosition] == ".": #Output the character signified by the cell at the pointer
		sys.stdout.write(chr(registry[registryPosition]))

	elif code[codePosition] == ",": #Input a character and store it in the cell at the pointer
		read = raw_input()
		registry[registryPosition] = ord(read[0])

	elif code[codePosition] == "[": #Jump past the matching ] if the cell under the pointer is 0
		if registry[registryPosition] == 0:
			brackets = 0
			codePosition += 1
			while codePosition < len(code): #Finding the right bracket to close
				if code[codePosition] == "]" and brackets == 0: 
					break
				elif code[codePosition] == "[":
					brackets += 1
				elif code[codePosition] == "]":
					brackets -= 1
				codePosition +=1

	elif code[codePosition] == "]": #Jump back to the matching [ if the cell under the pointer is nonzero
		if registry[registryPosition] != 0:
			brackets = 0
			codePosition -= 1
			while codePosition < len(code): #Finding the right bracket to continue looping
				if code[codePosition] == "[" and brackets == 0:
					break
				elif code[codePosition] == "]":
					brackets += 1
				elif code[codePosition] == "[":
					brackets -= 1
				codePosition -=1
	
	codePosition += 1