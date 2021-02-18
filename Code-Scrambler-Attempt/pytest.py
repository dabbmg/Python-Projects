import models


"""
TESTS TO ENSURE PROPER FUNCTIONALITY
"""
def test_encryption_decryptionn():
    phrases = ["Dog", "Liver", "Four"] #Testing even and uneven words with multiple vowels
    ende = models.EncryptDecrypt()
    encryptResult1 = ende.encrypt(phrases[0])
    encryptResult2 = ende.encrypt(phrases[1])
    encryptResult3 = ende.encrypt(phrases[2])
    decryptResult1 = ende.decrypt(encryptResult1)
    decryptResult2 = ende.decrypt(encryptResult2)
    decryptResult3 = ende.decrypt(encryptResult3)
    assert decryptResult1 == phrases[0]
    assert decryptResult2 == phrases[1]
    assert decryptResult3 == phrases[2]
    if decryptResult1 != phrases[0] or decryptResult2 != phrases[1]:
        print("Uneven words(Dog, Liver) issue")
    elif decryptResult3 != phrases[2]:
        print("Even word(Four) issue")
    else:
        print("Encryption and Decryption: Pass")



"""
RUN TESTS
"""
test_encryption_decryptionn()

