import enum


#Player Class
class Player:
    name = ""
    humanState = False
    COLOR = ''

    def constructor(self, newName, newState, newColor):
        self.name = newName
        self.humanState = newState
        self.COLOR = newColor


    def setName(self, newName):
        self.name = newName


    def getName(self):
        return self.name


    def setHumanState(self, newState):
        self.humanState = newState


    def getHumanState(self):
        return self.humanState


    def setColor(self, newColor):
        self.COLOR = newColor


    def getColor(self):
        return self.COLOR


#Board Class
class Board:

    def __init__(self):
            self.rows = 6
            self.cols = 7
            self.EMPTY = 'E'
            self.RED = 'R'
            self.YELLOW = 'Y'
            self.board = [[self.EMPTY] * self.rows for _ in range(self.cols)]

        
    def setPiece(self, columnNumber, color):
        columnNumber = columnNumber - 1
        for a in range(self.rows, 0, -1):
                check = self.board[a][columnNumber]
                if check == self.EMPTY and check != self.RED and check != self.YELLOW:
                    self.board[a][columnNumber] = color
                    print("\nPiece set as: " + color)
                    break


    def checkColumn(self, columnNumber):
        isFull = True
        for a in range(self.rows):
            if self.board[a][columnNumber - 1] == self.EMPTY:
                isFull = False
                break
        return isFull


    def checkForFour(self):
        directions = [(1,0), (1,-1), (1,1), (0,1)]
        for d in directions:
            dx = d[0]
            dy = d[1]
            for x in range(self.cols):
                for y in range(self.rows):
                    lastx = x + (3 * dx)
                    lasty = y + (3 * dy)
                    if 0 <= lastx and lastx < self.rows and 0 <= lasty and lasty < self.cols:
                        chk = self.board[x][y]
                        if (chk != self.EMPTY
                         and chk == self.board[x+dx][y+dy]
                          and chk == self.board[x+2*dx][y+2*dy]
                            and chk == self.board[lastx][lasty]):
                            if chk == self.RED:
                                return 1;
                            if chk == self.YELLOW:
                                return 2;
        return 0


    def printBoard(self):
        print("\nBoard\n")
        for inner_list in self.board:
            for j in inner_list:
                print(j,  end=" ")
            print()
                


    def newBoard(self):
        self.board.clear()
        self.board = [[self.EMPTY] * self.rows for _ in range(self.cols)]



#GameType Enum
class GameType(enum.Enum):
    PvP = 1
    PvC = 2
    CvC = 3

