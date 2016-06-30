theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
			'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
			'low-L': ' ', 'low-M': ' ', 'low-R': ' ' }

theBoardcr = {	'top-L': 0, 'top-M': 1, 'top-R': 2,
				'mid-L': 3, 'mid-M': 4, 'mid-R': 5,
				'low-L': 6, 'low-M': 7, 'low-R': 8 }

winningCombinations = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
listx = []
listo = []

x,o = 0,0
turn = 'X'



def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printBoard(theBoard)


for i in range(9):
	print('Turn for '+ turn + '. Make a move')
	move = raw_input()
	theBoard[move] = turn
	if turn == 'X':
		listx.append(theBoardcr[move])
		turn = 'O'
		x = x + 1
	else:
		listo.append(theBoardcr[move])
		turn = 'X'
		o = o + 1
	printBoard(theBoard)
	if(x >= 3):
		if(x == 3):
			if listx in winningCombinations:
				print("X won!!!")
				break



	if(o >= 3):
		if(o == 3):
			if listo in winningCombinations:
				print("O won!!!")
				break
