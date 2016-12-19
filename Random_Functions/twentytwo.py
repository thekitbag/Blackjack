#this programme will solve the game twenty-two
import random
possible_combos = [
[1,	11,	10],
[1,	12,	9],
[1,	13,	8],
[2,	7,	13],
[2,	8,	12],
[2,	9,	11],
[3,	6,	13],
[3,	7,	12],
[3,	8,	11],
[3,	9,	10],
[4,	5,	13],
[4,	6,	12],
[4,	7,	11],
[4,	8,	10],
[5,	6,	11],
[5,	7,	10],
[5,	8,	9],
[6,	7,	9],
]

combos = []

startswithone = []
startswithtwo = []
startswiththree = []
startswiththree = []
startswithfour = []
startswithfive = []
startswithsix = []
startswithseven = []
startswitheight = []
startswithnine = []
startswithten = []
startswitheleven = []
startswithtwelve = []
startswiththirteen = []

example = []

solution = []


for i in possible_combos:
	combos.append([i[0]] + [i[1]] + [i[2]])
	combos.append([i[0]] + [i[2]] + [i[1]])
	combos.append([i[1]] + [i[0]] + [i[2]])
	combos.append([i[1]] + [i[2]] + [i[0]])
	combos.append([i[2]] + [i[1]] + [i[0]])
	combos.append([i[2]] + [i[0]] + [i[1]])
		

for i in combos:
	if i[0] == 1:
		startswithone.append(i)
	elif i[0] == 2:
		startswithtwo.append(i)
	elif i[0] == 3:
		startswiththree.append(i)
	elif i[0] == 4:
		startswithfour.append(i)
	elif i[0] == 5:
		startswithfive.append(i)				
	elif i[0] == 6:
		startswithsix.append(i)
	elif i[0] == 7:
		startswithseven.append(i)
	elif i[0] == 8:
		startswitheight.append(i)
	elif i[0] == 9:
		startswithnine.append(i)
	elif i[0] == 10:
		startswithten.append(i)
	elif i[0] == 11:
		startswitheleven.append(i)
	elif i[0] == 12:
		startswithtwelve.append(i)
	else:
		startswiththirteen.append(i)	

#need to add the list comprehension for each list into each if statement
#need to remove the last number of the previous set from all startswiths except starts with that number



def chain(stage):
	def remover():
		global startswithone
		global startswithtwo
		global startswiththree
		global startswithfour
		global startswithfive
		global startswithsix
		global startswithseven
		global startswitheight
		global startswithnine
		global startswithten
		global startswitheleven
		global startswithtwelve
		global startswiththirteen
		startswithone = [x for x in startswithone if example[stage-1][1] not in x]
		startswithone = [x for x in startswithone if example[stage-1][0] not in x]
		startswithtwo = [x for x in startswithtwo if example[stage-1][1] not in x]
		startswithtwo = [x for x in startswithtwo if example[stage-1][0] not in x]
		startswiththree = [x for x in startswiththree if example[stage-1][1] not in x]
		startswiththree = [x for x in startswiththree if example[stage-1][0] not in x]
		startswithfour = [x for x in startswithfour if example[stage-1][1] not in x]
		startswithfour = [x for x in startswithfour if example[stage-1][0] not in x]
		startswithfive = [x for x in startswithfive if example[stage-1][1] not in x]
		startswithfive = [x for x in startswithfive if example[stage-1][0] not in x]		
		startswithsix = [x for x in startswithsix if example[stage-1][1] not in x]
		startswithsix = [x for x in startswithsix if example[stage-1][0] not in x]
		startswithseven = [x for x in startswithseven if example[stage-1][1] not in x]
		startswithseven = [x for x in startswithseven if example[stage-1][0] not in x]
		startswitheight = [x for x in startswitheight if example[stage-1][1] not in x]
		startswitheight = [x for x in startswitheight if example[stage-1][0] not in x]
		startswithnine = [x for x in startswithnine if example[stage-1][1] not in x]
		startswithnine = [x for x in startswithnine if example[stage-1][0] not in x]
		startswithten = [x for x in startswithten if example[stage-1][1] not in x]
		startswithten = [x for x in startswithten if example[stage-1][0] not in x]
		startswitheleven = [x for x in startswitheleven if example[stage-1][1] not in x]
		startswitheleven = [x for x in startswitheleven if example[stage-1][0] not in x]
		startswithtwelve = [x for x in startswithtwelve if example[stage-1][1] not in x]
		startswithtwelve = [x for x in startswithtwelve if example[stage-1][0] not in x]
		startswiththirteen = [x for x in startswiththirteen if example[stage-1][1] not in x]
		startswiththirteen = [x for x in startswiththirteen if example[stage-1][0] not in x]

	if example[stage-1][2] == 1:
		remover()
		if len(startswithone) != 0:
			example.append(random.choice(startswithone))
	if example[stage-1][2] == 2:
		remover()
		if len(startswithtwo) != 0:
			example.append(random.choice(startswithtwo))
	if example[stage-1][2] == 3:
		remover()
		if len(startswiththree) != 0:
			example.append(random.choice(startswiththree))		
	if example[stage-1][2] == 4:
		remover()
		if len(startswithfour) != 0:
			example.append(random.choice(startswithfour))
	if example[stage-1][2] == 5:
		remover()
		if len(startswithfive) != 0:
			example.append(random.choice(startswithfive))
	if example[stage-1][2] == 6:
		remover()
		if len(startswithsix) != 0:
			example.append(random.choice(startswithsix))
	if example[stage-1][2] == 7:
		remover()
		if len(startswithseven) != 0:
			example.append(random.choice(startswithseven))
	if example[stage-1][2] == 8:
		remover()
		if len(startswitheight) != 0:
			example.append(random.choice(startswitheight))
	if example[stage-1][2] == 9:
		remover()
		if len(startswithnine) != 0:
			example.append(random.choice(startswithnine))
	if example[stage-1][2] == 10:
		remover()
		if len(startswithten) != 0:
			example.append(random.choice(startswithten))
	if example[stage-1][2] == 11:
		remover()
		if len(startswitheleven) != 0:
			example.append(random.choice(startswitheleven))	
	if example[stage-1][2] == 12:
		remover()
		if len(startswithtwelve) != 0:
			example.append(random.choice(startswithtwelve))
	if example[stage-1][2] == 13:
		remover()
		if len(startswiththirteen) != 0:
			example.append(random.choice(startswiththirteen))
pegs = []											
used = []
unused = []
for i in range(1,14):
	pegs.append(i)
	

example.append(random.choice(combos))
chain(1)
chain(2)
if len(example) == 3:
	chain(3)
else: del example[:]
if len(example) == 4:
	chain(4)
else: del example[:]	
if len(example) == 5:
	chain(5)
else: del example[:]	

	
if len(example) > 4:
	for i in pegs:
		for j in example:
			if i in j:
				used.append(i)

	for i in pegs:
		if i not in used:
			unused.append(i)
	print example		
	print example[4][2], "X", example[0][0]
	print "unused=", unused
	for i in unused:
		if example[4][2] + example[0][0] + i == 22:
			print "ZOMG YOU FOLD A SOLUTION"
			solution.append(example)
			solution.append(unused)
			f = open("solutions.txt", "w")
			f.write(str(solution))
			f.write("\n")
			f.close()

		


