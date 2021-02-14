import models
import random


class ConnectFourGame:
    players = [models.Player() for _ in range(2)]
    board = models.Board()
    gameType = None
    exitState = False
    playerWin = False


    def run(self):
        print("\n------\nWelcome to Connect Four!\n------\n")
        self.userChoice()


    def runGame(self):
        self.nameInputs()
        self.board.__init__()
        self.runXvX()
        self.resetAllVariables()



    def userChoice(self):
        prompt = "What would you like to do?\nPlease only enter 1-4\n1.)Player vs Player\n2.)Player vs Computer\n3.)Computer vs Computer\n4.)Exit\n"
        userChoice = self.numberPrompt(prompt, 4, 1)
        if userChoice == 1:
            self.gameType = models.GameType.PvP
            self.runGame()
        elif userChoice == 2:
            self.gameType = models.GameType.PvC
            self.runGame()
        elif userChoice == 3:
            self.gameType = models.GameType.CvC
            self.runGame()
        elif userChoice == 4:
            print("\n---\nExiting\n---\n")
            self.setExit(True)



    def nameInputs(self):
        nameOne = input("\nWhat is the name of Player One? \n")
        isInvalid = len(nameOne) == 0
        if isInvalid == True:
            print("Ok, we will just use the default: Player1")
            nameOne = "Player1"
        nameTwo = input("\nWhat is the name of Player Two? \n")
        isInvalid = len(nameTwo) == 0
        if isInvalid == True:
            print("Ok, we will just use the default: Player2")
            nameTwo = "Player2"
        self.createPlayers(nameOne, nameTwo)


    def runXvX(self):
        rand = self.randomTurn()
        count = 0
        randSecond = 0
        if rand == 2:
            randSecond = 1
        else:
            randSecond = 2
        while self.playerWin == False:
            check = self.playerTurn(rand)
            count = count + 1
            if check == 1 or check == 2:
                self.board.printBoard()
                if check == 1:
                    print("\n------\n" + self.getPlayerName(1) + " WINS\n------")
                    self.playerWin = True
                    break
                elif check == 2:
                    print("\n------\n" + self.getPlayerName(2) + " WINS\n------")
                    self.playerWin = True
                    break
            checkTwo = self.playerTurn(randSecond)
            count = count + 1
            if checkTwo == 1 or checkTwo == 2:
                self.board.printBoard()
                if checkTwo == 1:
                    print("\n------\n" + self.getPlayerName(1) + " WINS\n------")
                    self.playerWin = True
                    break
                elif checkTwo == 2:
                    print("\n------\n" + self.getPlayerName(2) + " WINS\n------")
                    self.playerWin = True
                    break
            if count == 42:
                print("\n------\nDRAW\n------")
                self.playerWin = True
                break



    def playerTurn(self, player):
        if self.players[player - 1].getHumanState() == True:
            self.board.printBoard()
            self.humanMove(player)
        else:
            self.computerMove(player)
            self.board.printBoard()
        playerWhoWon = self.board.checkForFour()
        return playerWhoWon


    def randomTurn(self):
        p1, p2 = (1, 2)
        return random.choice([p1, p2])


    def humanMove(self, player):
        prompt = "\nWhich column would you like to player your piece in? (1-7) \n"
        isFull = True
        while isFull == True:
            playerMove = self.numberPrompt(prompt, 6, 1)
            isFull = self.board.checkColumn(playerMove)
            if isFull == True:
                print("\nColumn is full...try another...\n")
            else:
                self.board.setPiece(playerMove, self.players[player - 1].getColor())


    def computerMove(self, player):
        isFull = True
        isInvalid = True
        while isFull == True:
            while isInvalid == True:
                playerMove = random.randint(1, 6)
                isInvalid = playerMove > 6 or playerMove < 1
            isFull = self.board.checkColumn(playerMove)
        self.board.setPiece(playerMove, self.players[player - 1].getColor())


    def createPlayers(self, nameOne, nameTwo):
        if self.gameType == models.GameType.PvC:
            player1, player2 = (models.Player(), models.Player())
            player1.constructor(nameOne, True, 'R')
            player2.constructor(("Computer: " + nameTwo), False, 'Y')
            self.players.insert(0, player1)
            self.players.insert(0, player2)
        elif self.gameType == models.GameType.PvP:
            player1, player2 = (models.Player(), models.Player())
            player1.constructor(nameOne, True, 'R')
            player2.constructor(nameTwo, True, 'Y')
            self.players.insert(0, player1)
            self.players.insert(0, player2)
        elif self.gameType == models.GameType.CvC:
            player1, player2 = (models.Player(), models.Player())
            player1.constructor(("Computer: " + nameOne), False, 'R')
            player2.constructor(("Computer: " + nameTwo), False, 'Y')
            self.players.insert(0, player1)
            self.players.insert(0, player2)


    def getPlayerName(self, playerNumber):
        return self.players[playerNumber - 1].getName()


    def numberPrompt(self, inputPrompt, higherBound, lowerBound):
        isInvalid = True
        while isInvalid == True:
            userInput = input(inputPrompt)
            userChoice = int(userInput)
            isInvalid = userChoice < lowerBound or userChoice > higherBound
        return  userChoice


    def resetAllVariables(self):
        self.board.newBoard()
        self.players.clear()
        self.playerWin = False
        self.gameType = None


    def setExit(self, exitBool):
        self.exitState = exitBool


    def getExit(self):
        return self.exitState


    


