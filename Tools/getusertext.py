"""
Intended for command line use
-Mathew Dabb
"""
class UserText:
    def getUserText(prompt):
        tInput = ''
        isInvalid = True
        while isInvalid == True:
            tInput = input(prompt)
            isInvalid = len(tInput) == 0
            if isInvalid == True:
                print(prompt)
        return tInput