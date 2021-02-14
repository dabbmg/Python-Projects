import controllers



newGame = controllers.ConnectFourGame()
while newGame.getExit() == False:
    newGame.run()