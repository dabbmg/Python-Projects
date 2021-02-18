import models


"""
TESTS TO ENSURE PROPER FUNCTIONALITY
"""
def test_encryption_decryptionn():
    phrases = ["Dog", "Liver", "Four"] #Testing even and uneven words with multiple vowels
    print("Words to Test: " + phrases[0] + " - " + phrases[1] + " - " + phrases[2])
    ende = models.EncryptDecrypt()
    encryptResult1 = ende.encrypt(phrases[0])
    encryptResult2 = ende.encrypt(phrases[1])
    encryptResult3 = ende.encrypt(phrases[2])
    print("Encrypt Results: " + encryptResult1 + " - " + encryptResult2 + " - " + encryptResult3)
    decryptResult1 = ende.decrypt(encryptResult1)
    decryptResult2 = ende.decrypt(encryptResult2)
    decryptResult3 = ende.decrypt(encryptResult3)
    print("Decrypt Results: " + decryptResult1 + " - " + decryptResult2 + " - " + decryptResult3)


"""
RUN TESTS
"""
test_encryption_decryptionn()
