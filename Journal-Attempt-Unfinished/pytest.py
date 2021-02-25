import journalModels


dates = ["02/24/2021", "02/25/2021", "02/26/2021"]
text = ["Mat likes cats", "Mat likes dogs", "Mat likes GatoradeTM"]
jm = journalModels.Journal()

def test_journal_entry():
    jm.addPreviousEntriesOnStart()
    jm.addJournalEntry(dates[0], text[0])
    result = jm.searchJournalEntries(dates[0])
    if len(result) != None:
        print("Passed: " + result)
    else:
        print("Failed")


def test_journal_write_and_read():
    jm.writeJournalEntries()
    jm2 = journalModels.Journal()
    jm2.addPreviousEntriesOnStart()
    result = jm2.searchJournalEntries(dates[0])
    if len(result) != None:
        print("Passed: " + result)
    else:
        print("Failed")



"""
RUN TESTS
"""
test_journal_entry()
test_journal_write_and_read()
