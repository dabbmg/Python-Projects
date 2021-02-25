import journalModels
import re
from datetime import datetime

class UserInterface:
    journal = journalModels.Journal()
    exit = False

    def userChoice(self):
        prompt = "What would you like to do?\nPlease only enter 1-3\n1.)Create new Journal Entry\n2.)View previous Entry\n3.)Exit"
        userChoice = self.numberPrompt(prompt, 3, 1)
        if userChoice == 1:
            self.newJournalEntry()
        elif userChoice == 2:
            self.searchAndDisplay()
        elif userChoice == 3:
            print("\n---\nExiting...\n---")
            self.journal.writeJournalEntries()
            self.setExit(True)


    def newJournalEntry(self):
        date = self.getUserDate()
        text = self.getUserText()
        self.journal.addJournalEntry(date, text)
        print("Journal Entry Added")
    

    def getUserDate(self):
        dInput = ''
        isInvalid = True
        while isInvalid == True:
            dInput = input("Please enter the date for this entry in the format 'MM/DD/YYYY'")
            isInvalid = len(dInput) != 10
            if isInvalid == True:
                print("Please enter a valid date format, example '02/24/2021'")
            else:
                match = re.search(r'\d{2}-\d{2}-\d{4}', dInput)
                date = datetime.strptime(match.group(), '%m-%d-%Y').date()
                isInvalid = self.journal.checkDateTaken(date)
                if isInvalid == True:
                    print("That date is taken, try another. ")
        return date


    def getUserText(self):
        tInput = ''
        isInvalid = True
        while isInvalid == True:
            tInput = input("Please enter the text for this entry. ")
            isInvalid = len(tInput) == 0
            if isInvalid == True:
                print("You must enter something for this entry. ")
        return tInput


    def numberPrompt(self, prompt, higherB, lowerB):
        isInvalid = True
        while isInvalid == True:
            userInput = input(prompt)
            userChoice = int(userInput)
            isInvalid = userChoice < lowerB or userChoice > higherB
            if isInvalid == True:
                print("Please enter a number between " + str(lowerB) + " and " + str(higherB))
        return userChoice


    def searchAndDisplay(self):
        sInput = ''
        isInvalid = True
        while isInvalid == True:
            sInput = input("Please enter a date to search in format of 'MM/DD/YYYY")
            isInvalid = len(sInput) != 10
            if isInvalid == True:
                print("Please enter a valid date to search, example, '02/24/2021' ")
            else:
                match = re.search(r'\d{2}-\d{2}-\d{4}', sInput)
                date = datetime.strptime(match.group(), '%m-%d-%Y').date()
        print(self.journal.searchJournalEntries(date))


    def checkExit(self):
        return self.exit
    

    def setExit(self, newExit):
        self.exit = newExit