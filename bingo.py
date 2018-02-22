import random

#check for win of a player

def win_check(win, numleft):
	i = 0	
	while i < 100 and win == False:
		if numleft[i] == 0:
			win = True
		else:
			i += 1
	return win

#players check the number that was announced

def num_check(playerlist, numleft, num):
	for i in xrange(100):
		for j in xrange (5):
			if num == playerlist[i][j]:
				numleft[i] -= 1
	return numleft

#The 'bingo' game

def bingo(announcements):

	#Setting up a random 1-80 pool

	pool = []
	for i in xrange(1, 81):
		pool.append(i)
	random.shuffle(pool)

	#assigning numbers to 100 players

	players = []
	num_left = []
	for i in xrange(100):
		players.append(random.sample(pool,5))
		num_left.append(5)

	#The actual game

	bingo = False
	announcements = 0
	while bingo == False:
		announce = pool.pop()
		announcements += 1
		num_left = num_check(players, num_left, announce)
		if announcements > 4:
			bingo = win_check(bingo, num_left)
	return announcements

#repeating the game 1000 times

wins_count = 0
for i in xrange(1000):
	wins_count += bingo(wins_count)
wins_count /= 1000
print "After 1000 games of 'bingo', on average", wins_count, "numbers must be announced for someone to win."