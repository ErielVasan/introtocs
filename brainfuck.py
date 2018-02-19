import sys

#reading file. 

f = open(sys.argv[1], "r")
code = f.read() #assigning the contents of the file to one string.
f.close

#empty file error.

if code == "":
	print "Error! File is empty!"
	sys.exit

codePosition = 0
memory = [0]
memoryPosition = 0
output = ""

while codePosition < len(code):
	
	if code[codePosition] == "<": #pointer move to the left
		memoryPosition -= 1
		if memoryPosition < 0: #memory underflow check
			print "Error! Memory underflow!"
			sys.exit

	elif code[codePosition] == ">": #pointer move to the right
		memoryPosition += 1
		if len(memory) > memoryPosition:
			memory.append(0)
		if memoryPosition > 30000: #memory overflow check
			print "Error! Memory overflow!"
			sys.exit

	elif code[codePosition] == "+": #increase value of current cell
		memory[memoryPosition] += 1
		if memory[memoryPosition] > 255: #byte overflow, returns to 0
			memory[memoryPosition] = 0

	elif code[codePosition] == "-": #decrease value of current cell
		memory[memoryPosition] -= 1
		if memory[memoryPosition] < 0: #byte undeflow returns to 255
			memory[memoryPosition] = 255

	elif code[codePosition] == ".": #output current cell value in ASCII
		sys.stdout.write()

	elif code[codePosition] == ",": #input current cell ASCII character --> value

	elif code[codePosition] == "[":

	elif code[codePosition] == "]":

	codePosition += 1