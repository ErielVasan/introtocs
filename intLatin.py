def partchecker(latin, remainder, n):


#integer input and check

x = input("Give an integer between 1-1000000: ")
while (not (isinstance(x, int)) or x > 1000000 or x < 1):
	x = input("I asked for an integer between 1-1000000...: ")

#latin array

latin = ["[C][M]", "[D]", "[C][D]", "[C]", "[X][C]", "[L]", "[X][L]", "[X]", "M[X]", "[V]", "M[V]", "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]


#conversion process

if (x == 1000000):
	print("[M]")
else:
	for i in xrange(6, 0, -1):
		x = partchecker(latin, x, i)

