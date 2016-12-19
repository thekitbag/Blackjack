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

example = []
twolinks = []
threelinks = []
fourlinks = []
fivelinks = []
sixlinks = []
solutions = []


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

lst = startswithone



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



for i in combos:
	example.append(i)

for i in example:
	if example[example.index(i)][2] == 1:
		lst = startswithone
	if example[example.index(i)][2] == 2:
		lst = startswithtwo
	if example[example.index(i)][2] == 3:
		lst = startswiththree
	if example[example.index(i)][2] == 4:
		lst = startswithfour
	if example[example.index(i)][2] == 5:
		lst = startswithfive
	if example[example.index(i)][2] == 6:
		lst = startswithsix
	if example[example.index(i)][2] == 7:
		lst = startswithseven
	if example[example.index(i)][2] == 8:
		lst = startswitheight
	if example[example.index(i)][2] == 9:
		lst = startswithnine
	if example[example.index(i)][2] == 10:
		lst = startswithten
	if example[example.index(i)][2] == 11:
		lst = startswitheleven
	if example[example.index(i)][2] == 12:
		lst = startswithtwelve
	if example[example.index(i)][2] == 13:
		lst = startswiththirteen
	lst = [x for x in lst if example[example.index(i)][0] not in x]
	lst = [x for x in lst if example[example.index(i)][1] not in x]
	for j in lst:
		twolinks.append([i] + [j])



for i in twolinks:
	if twolinks[twolinks.index(i)][1][2] == 1:
		lst = startswithone
	if twolinks[twolinks.index(i)][1][2] == 2:
		lst = startswithtwo
	if twolinks[twolinks.index(i)][1][2] == 3:
		lst = startswiththree
	if twolinks[twolinks.index(i)][1][2] == 4:
		lst = startswithfour
	if twolinks[twolinks.index(i)][1][2] == 5:
		lst = startswithfive
	if twolinks[twolinks.index(i)][1][2] == 6:
		lst = startswithsix
	if twolinks[twolinks.index(i)][1][2] == 7:
		lst = startswithseven
	if twolinks[twolinks.index(i)][1][2] == 8:
		lst = startswitheight
	if twolinks[twolinks.index(i)][1][2] == 9:
		lst = startswithnine
	if twolinks[twolinks.index(i)][1][2] == 10:
		lst = startswithten
	if twolinks[twolinks.index(i)][1][2] == 11:
		lst = startswitheleven
	if twolinks[twolinks.index(i)][1][2] == 12:
		lst = startswithtwelve
	if twolinks[twolinks.index(i)][1][2] == 13:
		lst = startswiththirteen
	lst = [x for x in lst if twolinks[twolinks.index(i)][1][1] not in x]
	lst = [x for x in lst if twolinks[twolinks.index(i)][1][0] not in x]
	lst = [x for x in lst if twolinks[twolinks.index(i)][0][0] not in x]
	lst = [x for x in lst if twolinks[twolinks.index(i)][0][1] not in x]
	lst = [x for x in lst if twolinks[twolinks.index(i)][0][2] not in x]		
	for j in lst:
		threelinks.append(i + [j])

for i in threelinks:
	if threelinks[threelinks.index(i)][2][2] == 1:
		lst = startswithone
	if threelinks[threelinks.index(i)][2][2] == 2:
		lst = startswithtwo
	if threelinks[threelinks.index(i)][2][2] == 3:
		lst = startswiththree
	if threelinks[threelinks.index(i)][2][2] == 4:
		lst = startswithfour
	if threelinks[threelinks.index(i)][2][2] == 5:
		lst = startswithfive
	if threelinks[threelinks.index(i)][2][2] == 6:
		lst = startswithsix
	if threelinks[threelinks.index(i)][2][2] == 7:
		lst = startswithseven
	if threelinks[threelinks.index(i)][2][2] == 8:
		lst = startswitheight
	if threelinks[threelinks.index(i)][2][2] == 9:
		lst = startswithnine
	if threelinks[threelinks.index(i)][2][2] == 10:
		lst = startswithten
	if threelinks[threelinks.index(i)][2][2] == 11:
		lst = startswitheleven
	if threelinks[threelinks.index(i)][2][2] == 12:
		lst = startswithtwelve
	if threelinks[threelinks.index(i)][2][2] == 13:
		lst = startswiththirteen
	lst = [x for x in lst if threelinks[threelinks.index(i)][2][0] not in x]
	lst = [x for x in lst if threelinks[threelinks.index(i)][2][1] not in x]	
	lst = [x for x in lst if threelinks[threelinks.index(i)][1][0] not in x]
	lst = [x for x in lst if threelinks[threelinks.index(i)][1][1] not in x]
	lst = [x for x in lst if threelinks[threelinks.index(i)][1][2] not in x]
	lst = [x for x in lst if threelinks[threelinks.index(i)][0][0] not in x]
	lst = [x for x in lst if threelinks[threelinks.index(i)][0][1] not in x]
	lst = [x for x in lst if threelinks[threelinks.index(i)][0][2] not in x]		
	for j in lst:
		fourlinks.append(i + [j])

for i in fourlinks:
	if fourlinks[fourlinks.index(i)][3][2] == 1:
		lst = startswithone
	if fourlinks[fourlinks.index(i)][3][2] == 2:
		lst = startswithtwo
	if fourlinks[fourlinks.index(i)][3][2] == 3:
		lst = startswiththree
	if fourlinks[fourlinks.index(i)][3][2] == 4:
		lst = startswithfour
	if fourlinks[fourlinks.index(i)][3][2] == 5:
		lst = startswithfive
	if fourlinks[fourlinks.index(i)][3][2] == 6:
		lst = startswithsix
	if fourlinks[fourlinks.index(i)][3][2] == 7:
		lst = startswithseven
	if fourlinks[fourlinks.index(i)][3][2] == 8:
		lst = startswitheight
	if fourlinks[fourlinks.index(i)][3][2] == 9:
		lst = startswithnine
	if fourlinks[fourlinks.index(i)][3][2] == 10:
		lst = startswithten
	if fourlinks[fourlinks.index(i)][3][2] == 11:
		lst = startswitheleven
	if fourlinks[fourlinks.index(i)][3][2] == 12:
		lst = startswithtwelve
	if fourlinks[fourlinks.index(i)][3][2] == 13:
		lst = startswiththirteen
	lst = [x for x in lst if fourlinks[fourlinks.index(i)][3][0] not in x]
	lst = [x for x in lst if fourlinks[fourlinks.index(i)][3][1] not in x]	
	lst = [x for x in lst if fourlinks[fourlinks.index(i)][2][0] not in x]
	lst = [x for x in lst if fourlinks[fourlinks.index(i)][2][1] not in x]
	lst = [x for x in lst if fourlinks[fourlinks.index(i)][2][2] not in x]	
	lst = [x for x in lst if fourlinks[fourlinks.index(i)][1][0] not in x]
	lst = [x for x in lst if fourlinks[fourlinks.index(i)][1][1] not in x]
	lst = [x for x in lst if fourlinks[fourlinks.index(i)][1][2] not in x]
	lst = [x for x in lst if fourlinks[fourlinks.index(i)][0][0] not in x]
	lst = [x for x in lst if fourlinks[fourlinks.index(i)][0][1] not in x]
	lst = [x for x in lst if fourlinks[fourlinks.index(i)][0][2] not in x]		
	for j in lst:
		fivelinks.append(i + [j])		

for i in fivelinks:
	if fivelinks[fivelinks.index(i)][4][2] == 1:
		lst = startswithone
	if fivelinks[fivelinks.index(i)][4][2] == 2:
		lst = startswithtwo
	if fivelinks[fivelinks.index(i)][4][2] == 3:
		lst = startswiththree
	if fivelinks[fivelinks.index(i)][4][2] == 4:
		lst = startswithfour
	if fivelinks[fivelinks.index(i)][4][2] == 5:
		lst = startswithfive
	if fivelinks[fivelinks.index(i)][4][2] == 6:
		lst = startswithsix
	if fivelinks[fivelinks.index(i)][4][2] == 7:
		lst = startswithseven
	if fivelinks[fivelinks.index(i)][4][2] == 8:
		lst = startswitheight
	if fivelinks[fivelinks.index(i)][4][2] == 9:
		lst = startswithnine
	if fivelinks[fivelinks.index(i)][4][2] == 10:
		lst = startswithten
	if fivelinks[fivelinks.index(i)][4][2] == 11:
		lst = startswitheleven
	if fivelinks[fivelinks.index(i)][4][2] == 12:
		lst = startswithtwelve
	if fivelinks[fivelinks.index(i)][4][2] == 13:
		lst = startswiththirteen
	lst = [x for x in lst if fivelinks[fivelinks.index(i)][4][0] not in x]
	lst = [x for x in lst if fivelinks[fivelinks.index(i)][4][1] not in x]	
	lst = [x for x in lst if fivelinks[fivelinks.index(i)][3][0] not in x]
	lst = [x for x in lst if fivelinks[fivelinks.index(i)][3][1] not in x]
	lst = [x for x in lst if fivelinks[fivelinks.index(i)][3][2] not in x]	
	lst = [x for x in lst if fivelinks[fivelinks.index(i)][2][0] not in x]
	lst = [x for x in lst if fivelinks[fivelinks.index(i)][2][1] not in x]
	lst = [x for x in lst if fivelinks[fivelinks.index(i)][2][2] not in x]	
	lst = [x for x in lst if fivelinks[fivelinks.index(i)][1][0] not in x]
	lst = [x for x in lst if fivelinks[fivelinks.index(i)][1][1] not in x]
	lst = [x for x in lst if fivelinks[fivelinks.index(i)][1][2] not in x]
	lst = [x for x in lst if fivelinks[fivelinks.index(i)][0][1] not in x]
	lst = [x for x in lst if fivelinks[fivelinks.index(i)][0][2] not in x]		
	for j in lst:
		sixlinks.append(i + [j])	
	

for i in sixlinks:
	if i[0][0] == i[5][2]:
		solutions.append(i)




f = open("solutions.txt", "w")
for i in solutions:
	f.write(str(i))
	f.write("\n")	
f.close()

"""
lst = [x for x in lst if fourlinks[fourlinks.index(i)][4][0] not in x]
	lst = [x for x in lst if fourlinks[fourlinks.index(i)][4][1] not in x]	
	lst = [x for x in lst if fourlinks[fourlinks.index(i)][3][0] not in x]
	lst = [x for x in lst if fourlinks[fourlinks.index(i)][3][1] not in x]
	lst = [x for x in lst if fourlinks[fourlinks.index(i)][3][2] not in x]	
	lst = [x for x in lst if fourlinks[fourlinks.index(i)][2][0] not in x]
	lst = [x for x in lst if fourlinks[fourlinks.index(i)][2][1] not in x]
	lst = [x for x in lst if fourlinks[fourlinks.index(i)][2][2] not in x]	
	lst = [x for x in lst if fourlinks[fourlinks.index(i)][1][0] not in x]
	lst = [x for x in lst if fourlinks[fourlinks.index(i)][1][1] not in x]
	lst = [x for x in lst if fourlinks[fourlinks.index(i)][1][2] not in x]
	lst = [x for x in lst if fourlinks[fourlinks.index(i)][0][0] not in x]
	lst = [x for x in lst if fourlinks[fourlinks.index(i)][0][1] not in x]
	lst = [x for x in lst if fourlinks[fourlinks.index(i)][0][2] not in x]		
	for j in lst:
		sixlinks.append(i + [j])	


"""