#integer input and check

x = input("Give an integer between 1-1000000: ")

while (not (isinstance(x, int)) or x > 1000000 or x < 1):
	x = input("I asked for an integer between 1-1000000...: ")

#latin list

latin = ["[C][M]", "[D]", "[C][D]", "[C]", "[X][C]", "[L]", "[X][L]", "[X]", "M[X]", "[V]", "M[V]", "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]


#conversion process

latinString = ""

if (x == 1000000):
	latinString = "[M]"

else:
	for n in xrange(len(str(x)), 0, -1):
		iCheck = False
		
		while (x / 10 ** (n - 1) > 0):
			
			if (iCheck == True): #check if there has been another check before
				latinString += latin[(6 - n) * 4 + 3]
				x -= 1* 10 ** (n - 1)
			
			elif (x - 9 * 10 ** (n - 1) >= 0): #check of 9s
				latinString += latin[(6 - n) * 4 + 0]
				x -= 9 * 10 ** (n - 1)
				break			

			elif (x - 5 * 10 ** (n - 1) >= 0): #check of 5s
				latinString += latin[(6 - n) * 4 + 1]
				x -= 5 * 10 ** (n - 1)
				iCheck = True
			
			elif (x - 4 * 10 ** (n - 1) >= 0): #check of 4s
				latinString += latin[(6 - n) * 4 + 2]
				x -= 4 * 10 ** (n - 1)
				break

			else				   #check of 1s
				latinString += latin[(6 - n) * 4 + 3]
				x -= 1 * 10 ** (n - 1)
				iCheck = True

print latinString
