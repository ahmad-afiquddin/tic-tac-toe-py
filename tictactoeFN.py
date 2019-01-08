import random

##HELPS WITH COMLOGIC##
coordBoard = [[(1,3),(2,3),(3,3)],[(1,2),(2,2),(3,2)],[(1,1),(2,1),(3,1)]]

##GAMEBOARD CLASS##
class gameBoard():
    def __init__(self):
        self.board = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]

        self.player = 'x'
        self.com = 'o'

    def dispBoard(self):
        print('Current Board: ')
        for row in self.board:
            rowStr = ''
            for col in row:
                rowStr += ''.join(['|', col, '|'])
            print(rowStr)

    def clearBoard(self):
        self.board = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]

    def placeBoard(self, coords, token):

        xVal = coords[0] - 1
        yVal = 3 - coords[1]
        if token == self.player:
            if (xVal < 0 or xVal > 2 or yVal < 0 or yVal > 2):
                print('COORDINATES OUT OF RANGE. PLEASE ENTER CORRECTLY')
                return False
            elif (self.board[yVal][xVal] == ' '):
                self.board[yVal][xVal] = token
                return True
            elif (self.board[yVal][xVal] != ' '):
                print('COORDINATES HAS BEEN FILLED. PICK ANOTHER ONE')
                return False
        elif token == self.com:
            if (xVal < 0 or xVal > 2 or yVal < 0 or yVal > 2):
                return False
            elif (self.board[yVal][xVal] == ' '):
                self.board[yVal][xVal] = token
                return True
            elif (self.board[yVal][xVal] != ' '):
                return False



def playGame():
    reFlag = True
    mode = 1
    board = gameBoard()
    while (reFlag):
        board.clearBoard()
        turn = random.randint(1,10000) % 2
        playerInput(1, turn)
        if (turn == 0):
            board.dispBoard()
            coords = playerInput(2, turn)
            while (not board.placeBoard(coords, 'x')):
                board.dispBoard()
                coords = playerInput(2, turn)
            board.dispBoard()
        elif (turn == 1) :
            coords = playerInput(2, turn)
            comLogic(board)
            board.dispBoard()

        turn += 1
        turn = turn % 2

        while (scanGame(board) == 0):
            if (turn == 0):
                coords = playerInput(2, turn)
                while (not board.placeBoard(coords, 'x')):
                    board.dispBoard()
                    coords = playerInput(2, turn)
                board.dispBoard()
            elif (turn == 1) :
                coords = playerInput(2, turn)
                comLogic(board)
                board.dispBoard()
            turn += 1
            turn = turn % 2

        reFlag = playerInput(3, turn)


##PROMPTS INPUT FROM USER##
def playerInput(mode, turn):
    if (mode == 1):
        print("WELCOME TO TIC-TAC-TOE. YOUR TOKEN IS x. COM'S TOKEN IS o")
        if (turn == 0):
            print('PLAYERS TURN')
        if (turn == 1):
            print("COM'S TURN")

    if (mode == 2):
        if (turn == 0):
            incFlag = 1
            print('YOUR TURN. ENTER COORDINATES IN THIS FORMAT X,Y: ')
            while(incFlag):
                try:
                    coords = input()
                    coords = coords.split(',')
                    coords = [int(x.strip()) for x in coords]
                    incFlag = 0
                except:
                    print('FORMAT IS X,Y E.G 1,1')

            return coords
        if (turn == 1):
            print("COM'S TURN")
    if (mode == 3):
        incFlag = 1
        print('GAME OVER, PLAY AGAIN? (y/n)')
        while (incFlag):
            response = input()
            if (response != 'y' and response != 'n'):
                incFlag = 1
                print('PLEASE TYPE y OR n')
            else:
                if (response == 'y'):
                    return True
                elif (response == 'n'):
                    print('BYE BYE')
                    return False
                incFlag = 0

##LOW LEVEL LOGIC USED, FOR BETTER LOGIC PLEASE IMPLEMENT A GAME TREE##
def comLogic(board):
    coordsDict = scanTwo(board)
    if (coordsDict.get(board.com)):
        coordList = list(set(coordsDict.get(board.com)))
        board.placeBoard(coordList[0], board.com)
    elif (coordsDict.get(board.player)):
        coordList = list(set(coordsDict.get(board.player)))
        board.placeBoard(coordList[0], board.com)
    else:
        xVal = random.randint(1,10000) % 3 + 1
        yVal = random.randint(1,10000) % 3 + 1
        while (not board.placeBoard((xVal, yVal),board.com)):
            xVal = random.randint(1,10000) % 3 + 1
            yVal = random.randint(1,10000) % 3 + 1

##HELPS WITH COMLOGIC, SCANS IF THERE ARE TWO TOKENS WITHIN A ROW, COL, OR DIAG##
def scanTwo(board):
    retDict = {}
    rotBoard = flipBoard(board.board)
    diaBoard = diagBoard(board.board)
    xTok = 0
    oTok = 0
    bTok = 0
    bCoords = []
    for ind in range(len(board.board)):
        for indTok in range(len(board.board[ind])):
            token = board.board[ind][indTok]
            if token == 'x':
                xTok += 1
            elif token == 'o':
                oTok += 1
            elif token == ' ':
                bCoords = list(map(list, zip(*coordBoard)))[indTok][ind]
                bTok += 1
        if (xTok == 2 and bTok == 1):
            if (retDict.get('x')):
                xList = retDict.get('x')
                xList.append(bCoords)
                retDict.update({'x':xList})
            else:
                retDict.update({'x':[bCoords]})
                print(retDict.get('x'))
        elif (oTok == 2 and bTok == 1):
            if (retDict.get('o')):
                oList = retDict.get('o')
                oList.append(bCoords)
                retDict.update({'o':oList})
            else:
                retDict.update({'o':[bCoords]})
        xTok = 0
        oTok = 0
        bTok = 0
        bCoords = ()

    for ind in range(len(rotBoard)):
        for indTok in range(len(rotBoard[ind])):
            token = rotBoard[ind][indTok]
            if token == 'x':
                xTok += 1
            elif token == 'o':
                oTok += 1
            elif token == ' ':
                bCoords = flipBoard(coordBoard)[ind][indTok]
                bTok += 1
        if (xTok == 2 and bTok == 1):
            if (retDict.get('x')):
                xList = retDict.get('x')
                xList.append(bCoords)
                retDict.update({'x':xList})
            else:
                retDict.update({'x':[bCoords]})
        elif (oTok == 2 and bTok == 1):
            if (retDict.get('o')):
                oList = retDict.get('o')
                oList.append(bCoords)
                retDict.update({'o':oList})
            else:
                retDict.update({'o':[bCoords]})
        xTok = 0
        oTok = 0
        bTok = 0
        bCoords = ()

    for ind in range(len(diaBoard)):
        for indTok in range(len(diaBoard[ind])):
            token = diaBoard[ind][indTok]
            if token == 'x':
                xTok += 1
            elif token == 'o':
                oTok += 1
            elif token == ' ':
                bCoords = diagBoard(coordBoard)[ind][indTok]
                bTok += 1
        if (xTok == 2 and bTok == 1):
            if (retDict.get('x')):
                xList = retDict.get('x')
                xList.append(bCoords)
                retDict.update({'x':xList})
            else:
                retDict.update({'x':[bCoords]})
        elif (oTok == 2 and bTok == 1):
            if (retDict.get('o')):
                oList = retDict.get('o')
                oList.append(bCoords)
                retDict.update({'o':oList})
            else:
                retDict.update({'o':[bCoords]})
        xTok = 0
        oTok = 0
        bTok = 0
        bCoords = ()

    return retDict

##SCANS GAMEBOARD FOR GAME OVER##
##0 FOR NO, 1 FOR FULL BOARD, 2 FOR A WINNER##
def scanGame(board):
    for row in board.board:
        if (row[0] == row[1] and row[1] == row[2] and row[2] != ' '):
            return 2
    for col in flipBoard(board.board):
        if (col[0] == col[1] and col[1] == col[2] and col[2] != ' '):
            return 2
    for diag in diagBoard(board.board):
        if (diag[0] == diag[1] and diag[1] == diag[2] and diag[2] != ' '):
            return 2

    for row in board.board:
        for col in row:
            if col == ' ':
                return 0

    return 1

##ROTATES GAMEBOARD - HELPS ME CODE##
def flipBoard(board):
    retList = list(map(list, zip(*board)))
    return retList

##RETURNS LIST OF DIAGONALS - HELPS ME CODE##
def diagBoard(board):
    retList = [[board[2][0], board[1][1], board[0][2]], [board[2][2],board[1][1], board[0][0]]]
    return retList

if __name__ == '__main__':
    playGame()


