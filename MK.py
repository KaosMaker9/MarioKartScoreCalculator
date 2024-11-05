def calc(scores):
    a = int(scores[0])
    b = int(scores[1])
    c = int(scores[2])
    d = int(scores[3])

    total = 0

    if(a == 1 or b == 1 or c == 1 or d == 1):
        total += 10
    if(a == 2 or b == 2 or c == 2 or d == 2):
        total += 8
    if(a == 3 or b == 3 or c == 3 or d == 3):
        total += 6
    if(a == 4 or b == 4 or c == 4 or d == 4):
        total += 5
    if(a == 5 or b == 5 or c == 5 or d == 5):
        total += 4
    if(a == 6 or b == 6 or c == 6 or d == 6):
        total += 3
    if(a == 7 or b == 7 or c == 7 or d == 7):
        total += 2
    if(a == 8 or b == 8 or c == 8 or d == 8):
        total += 1
    return total

total = 0
opponent = 0

for x in range(1, 5):
	game = input("Enter places for race " + str(x) + ": ")
	scores = game.split()

	us = calc(scores)

	print("We got " + str(us) + " points this race")
	opponent += (39 - us)
	
	difference = us - (39 - us)
	if(difference > 0):
		print("We outscored the opponent by " + str(difference) + " points")
	else:
		print("Our opponents outscored us by " + str(-difference) + " points")
	
	total += us

	print("Us: " + str(total) + " Them: " + str(opponent))