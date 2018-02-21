import sys

#reading file. 

f = open(sys.argv[1], "r")
code = f.read() #assigning the contents of the file to one string
f.close

#empty file check

if code == "":
	print "Error! File is empty!"
	sys.exit

codePosition = 0
register = [0]
registerPosition = 0

while codePosition < len(code):

	if code[codePosition] == ">": #pointer move to the right
		registerPosition += 1
		if len(register) <= registerPosition:
			register.append(0)
		if registerPosition > 30000: #register overflow check
			print "Error! Register overflow!"
			sys.exit
	
	elif code[codePosition] == "<": #pointer move to the left
		registerPosition -= 1
		if registerPosition < 0: #register underflow check
			print "Error! Register underflow!"
			sys.exit

	elif code[codePosition] == "+": #increase value of current cell
		register[registerPosition] += 1
		if register[registerPosition] > 255: #byte overflow, returns to 0
			register[registerPosition] = 0

	elif code[codePosition] == "-": #decrease value of current cell
		register[registerPosition] -= 1
		if register[registerPosition] < 0: #byte undeflow returns to 255
			register[registerPosition] = 255

	elif code[codePosition] == ".": #output current cell value in ASCII
		sys.stdout.write(chr(register[registerPosition]))

	elif code[codePosition] == ",": #input current cell ASCII character --> value
		read = raw_input()
		register[registerPosition] = ord(read[0])

	elif code[codePosition] == "[":

	elif code[codePosition] == "]":

	codePosition += 1