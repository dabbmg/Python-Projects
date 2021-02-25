import consoleInterface

ui = consoleInterface.UserInterface()
ui.journal.addPreviousEntriesOnStart()
while ui.checkExit == False:
    ui.userChoice()