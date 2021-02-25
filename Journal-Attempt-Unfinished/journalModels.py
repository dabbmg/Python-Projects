import json
import os
"""
Try creating a Journal as a dictionary for python
"""
class Journal:

    """
    Dictonary acts as pages with dates and text
    """
    journalEntries = {}
    

    def addJournalEntry(self, date, text):
        self.journalEntries[date] = text


    def checkDateTaken(self, date):
        for i in self.journalEntries:
            if i == date:
                return True
        return False
    

    def searchJournalEntries(self, date):
        searchResult = None
        for i in self.journalEntries:
            if i == date:
                searchResult = "Entry for " + i + "\n\t" + self.journalEntries[i]
                break
            else:
                searchResult = "Couldn't find entry for date given. "
        return searchResult
    

    def addPreviousEntriesOnStart(self):
        if os.stat('journal.txt').st_size == 0:
            print("\n---\nNo previous Journal entries to load\n---\n")
        else:
            with open('journal.txt', 'r') as f:
                dict = json.loads(f.read())
                self.journalEntries = dict
            if len(self.journalEntries) != 0:
                length = len(self.journalEntries)
                string = "\n---\nLoaded + " + str(length) + " entries for dates:"
                for i in self.journalEntries:
                    string += "\n\t" + i
                string += "\n---\n"
                print(str)
            else:
                print("\n---\nNo previous Journal entries to load\n---\n")
    

    def writeJournalEntries(self):
        with open('journal.txt', 'w') as f:
            f.write("")
        with open('journal.txt', 'w') as f:
            f.write(json.dumps(self.journalEntries))