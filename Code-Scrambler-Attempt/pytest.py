import models


"""
TESTS TO ENSURE PROPER FUNCTIONALITY
"""
def test_encryption_decryptionn():
    phrases = ["Dog", "Liver", "Four"] #Testing even and uneven words with multiple vowels
    ende = models.EncryptDecrypt()
    encryptResults = [ende.encrypt(phrases[0]), ende.encrypt(phrases[1]), ende.encrypt(phrases[2])]
    decryptResults = [ende.decrypt(encryptResults[0]), ende.decrypt(encryptResults[1]), ende.decrypt(encryptResults[2])]
    assert decryptResults[0] == phrases[0]
    assert decryptResults[1] == phrases[1]
    assert decryptResults[2] == phrases[2]
    if decryptResults[0] != phrases[0] or decryptResults[1] != phrases[1]:
        print("Uneven words(Dog, Liver) issue")
    elif decryptResults[2] != phrases[2]:
        print("Even word(Four) issue")
    else:
        print("Encryption and Decryption: Pass")



"""
RUN TESTS
"""
test_encryption_decryptionn()

