import random
import math


class EncryptDecrypt:
    """
    Takes two statements:
        -The phrase the user entered
        -If the user is encrypting or decrypting
    Then runs it through the process of encrypting or decrypting
    """


    def encrypt(self, strPhrase):
        boolDecrypt = False
        endResult1 = self.cutter(strPhrase, boolDecrypt)
        endResult2 = self.doubler(endResult1, boolDecrypt)
        endResult3 = self.vowelReplacer(endResult2, boolDecrypt)
        endResult4 = self.codeAdder(endResult3, boolDecrypt)
        return endResult4
    

    def decrypt(self, strPhrase):
        boolDecrypt = True
        endResult1 = self.codeAdder(strPhrase, boolDecrypt)
        endResult2 = self.vowelReplacer(endResult1, boolDecrypt)
        endResult3 = self.doubler(endResult2, boolDecrypt)
        endResult4 = self.cutter(endResult3, boolDecrypt)
        return endResult4


    """
    Doubler
    -Encrypt: Takes given string and doubles it
    -Decrypt: Takes given string and cuts it in half
    """
    def doubler(self, phrase, boolDecrypt):
        if boolDecrypt == True:
            return phrase[0:len(phrase)//2]
        else:
            phraseDouble = phrase
            endProduct = phrase + phraseDouble
            return endProduct


    """
    Cutter
    -Encrypt: Takes given string and puts the front half at the back half
    -Decrypt: Takes the back half and returns it to the front half
    """
    def cutter(self, phrase, boolDecrpyt):
        if len(phrase) % 2 == 0:
            length = len(phrase)
            middle = int(length / 2.0)
            parts = []
            parts.append(phrase[:middle])
            parts.append(phrase[middle:])
            endProduct = parts[1] + parts[0]
            return endProduct
        else:
            length = len(phrase)
            middle = length / 2.0
            roundedMiddle = int(math.floor(middle))
            if boolDecrpyt == True:
                roundedMiddle = int(math.floor(middle) + 1)
            parts = []
            parts.append(phrase[:roundedMiddle])
            parts.append(phrase[roundedMiddle:])
            endProduct = parts[1] + parts[0]
            return endProduct


    """
    VowelReplacer
    -Encrypt & Decrypt:
        A to E
        E to I
        I to O
        O to U
        U to A
    """
    def vowelReplacer(self, phrase, boolDecrypt):
        values = []
        upperCase = ['A','E','I','O','U']
        lowerCase = ['a','e','i','o','u']
        endProduct = phrase
        if boolDecrypt == False:
            values.extend((1,2,3,4,0))
        else:
            values.extend((4,0,1,2,3))
        for e in phrase:
            e.replace(e, self.shiftValue(e, upperCase, values))
        for b in phrase:
            b.replace(b, self.shiftValue(b, lowerCase, values))
        return endProduct

    def shiftValue(self, ch, vowels, values):
        if ch == vowels[0]:
                ch = vowels[int(values[0])]
        elif ch == vowels[1]:
                ch = vowels[int(values[1])]
        elif ch == vowels[2]:
                ch = vowels[int(values[2])]
        elif ch == vowels[3]:
                ch = vowels[int(values[3])]
        elif ch == vowels[4]:
                ch = vowels[int(values[4])]
        return ch



    """
    Code Adder
    -Encrypt: Adds Random Code to end of Phrase
    -Decrypt: Find and removes random code from end of Phrase
    """
    def codeAdder(self, phrase, boolDecrypt):
        code = '$' + str(random.randint(1, 99))
        if boolDecrypt == False:
            endProduct = phrase + code
            return endProduct
        else:
            find = phrase.index('$')
            endProduct = phrase[0:find]
            return endProduct