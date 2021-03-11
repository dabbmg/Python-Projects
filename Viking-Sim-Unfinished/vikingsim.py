from Tools.filehandler import FileHandler
from Tools.getusertext import UserText
from Tools.numberprompt import NumberPrompt
GODS = 'Odin', 'Thor', 'Loki', 'Freya'
INVENTORYITEMS = 'Gold', 'Silver', 'Slaves', 'Knowledge', 'Weapons'
boolExit = False
firstTime = None

def readOnStart(self):
    player = FileHandler.readObjectFromFile(self, 'C:\\VikingSim')
    if(player == None):
        firstTime = True
    else:
        firstTime = False
        print("\nViking Found:\n" + player.toString())
    if(firstTime == True):
        self.createPlayerViking()
