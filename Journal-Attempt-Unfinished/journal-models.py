import csv
"""
Acts as a 'page' with the date and entry text
"""
class JournalEntry:

    def ___init___(self, newDate, newText):
        self.date = newDate
        self.entryText = newText

    def getDate(self):
        return self.date

    def setDate(self, newDate):
        self.date = newDate

    def getEntryText(self):
        return self.entryText

    def setEntryText(self, newText):
        self.entryText = newText

    def toString(self):
        return "\n---\nEntry for " + self.date + "\n\t" + self.entryText + "\n---\n"


"""
Acts as an array / book of JournalEntry pages.
    -Serializes objects into a txt file for later viewing
"""
class Journal:

    journalEntries = []

    def addJournalEntry(self, newEntry):
        self.journalEntries.append(newEntry)
        print("Entry added for date: " + newEntry.date())

    def checkDateTaken(self, date):
        for i in self.journalEntries:
            if self.journalEntries[i].getDate() == date:
                return True
        return False
    
    def searchJournalEntries(self, date):
        searchResult = ''
        for i in self.journalEntries:
            if self.journalEntries[i].getDate() == date:
                searchResult = self.journalEntries[i].toString()
                break
            else:
                searchResult = "Couldn't find entry for date given"
        return searchResult
    
    def addPreviousEntriesOnStart(self):
        with open('journal.txt', "w") as journal:
            reader = csv.reader(journal)
            for row in reader:
                self.journalEntries.append(row)
        if len(self.journalEntries) != 0:
            str = "\n---\nLoaded + " + str(len(self.journalEntries)) + " entries for dates:"
            for i in self.journalEntries:
                str += "\n\t" + self.journalEntries[i].getDate()
            str += "\n---\n"
            print(str)
        else:
            print("\n---\nNo previous Journal entries to load\n---\n")

    def writeJournalEntries(self):
        with open('journal.txt', 'w') as journal:
            journal.write("")
        with open('journal.txt', 'w') as journal:
            journal.write('\n'.join(self.journalEntries))