"""
Intended for command line use
-Mathew Dabb
"""
class NumberPrompt:
    def numberPrompt(prompt, higherB, lowerB):
        isInvalid = True
        while isInvalid == True:
            userInput = input(prompt)
            userChoice = int(userInput)
            isInvalid = userChoice < lowerB or userChoice > higherB
            if isInvalid == True:
                print("Please enter a number between " + str(lowerB) + " and " + str(higherB))
        return userChoice