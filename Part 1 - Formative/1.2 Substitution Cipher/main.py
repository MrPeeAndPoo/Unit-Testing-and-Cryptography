# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def sub_encode(text, codebet):
    newString = ""
    for letter in text:
        newString += codebet[alpha.find(letter)]
    return newString


def sub_decode(text, codebet):
    newString = ""
    for letter in text:
        newString += alpha[codebet.find(letter)]
    return newString


test = "HELLOWORLD"
cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
enc = sub_encode(test, cipher_alphabet)
dec = sub_decode(enc, cipher_alphabet)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
