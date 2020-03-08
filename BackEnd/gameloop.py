import random

def getWordList():
	filename = "nouns.txt"
	with open(filename) as f: 
		words = f.read().splitlines()
	return words

def getMaxTurns():
	if (len(players) % 2 == 0):
		return len(players) - 1
	else:
		return len(players)

def intializeSequences():
	for i in range(len(players)):
		sequences.append([random.choice(wordList)])

def sendItemsToPlayers():
	rotatedPlayerList = players[currentTurn:] + players[:currentTurn]
	#for i in range(len(players)):
		# print("Sending [" + sequences[i][currentTurn] + "] to " + rotatedPlayerList[i])

def waitForResponsesFromPlayers():
	rotatedPlayerList = players[currentTurn:] + players[:currentTurn]
	for i in range(len(players)):
		if (currentTurn % 2 == 0):
			sequences[i].append(rotatedPlayerList[i] + "'s drawing of " + sequences[i][currentTurn])
		else:
			sequences[i].append(rotatedPlayerList[i] + "'s guess of " + sequences[i][currentTurn])


wordList = getWordList()
players = ["toffler", "bloomfeld", "mullett", "kopen", "shulman"]
sequences = []
currentTurn = 0
maxTurns = getMaxTurns()

intializeSequences()
while (currentTurn < maxTurns):
	sendItemsToPlayers()
	waitForResponsesFromPlayers()
	currentTurn += 1
for sequence in sequences:
	print(sequence)