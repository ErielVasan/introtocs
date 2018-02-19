import sys

#reading file. 

f = open(sys.argv[1], "r")
code = f.read() #assigning the contents of the file to one string.
f.close

#empty file error.

if code == "":
	print "Error! File is empty!"
	sys.exit