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
register = [0]
registerPosition = 0

#Code Execution

while codePosition < len(code):

	if code[codePosition] == ">": #Move the pointer to the right
		registerPosition += 1
		if len(register) <= registerPosition:
			register.append(0)
		if registerPosition > 30000: #Register overflow check
			print "Error! Register overflow!"
			sys.exit
	
	elif code[codePosition] == "<": #Move the pointer to the left
		registerPosition -= 1
		if registerPosition < 0: #Register underflow check
			print "Error! Register underflow!"
			sys.exit

	elif code[codePosition] == "+": #Increment the memory cell under the pointer
		register[registerPosition] += 1
		if register[registerPosition] > 255: #Byte overflow, returns to 0
			register[registerPosition] = 0

	elif code[codePosition] == "-": #Decrement the memory cell under the pointer
		register[registerPosition] -= 1
		if register[registerPosition] < 0: #Byte undeflow returns to 255
			register[registerPosition] = 255

	elif code[codePosition] == ".": #Output the character signified by the cell at the pointer
		sys.stdout.write(chr(register[registerPosition]))

	elif code[codePosition] == ",": #Input a character and store it in the cell at the pointer
		read = raw_input()
		register[registerPosition] = ord(read[0])

	elif code[codePosition] == "[": #Jump past the matching ] if the cell under the pointer is 0
		if register[registerPosition] == 0:
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
		if register[registerPosition] != 0:
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