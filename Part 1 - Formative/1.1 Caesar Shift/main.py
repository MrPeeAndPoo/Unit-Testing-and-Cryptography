# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_encode(text, n):
    newString = ""
    for letter in text:
        index = alpha.find(letter)
        newString += alpha[(index + n) % 26]
    return newString


def caesar_decode(text, n):
    newString = ""
    for letter in text:
        index = alpha.find(letter)
        newString += alpha[(index - n) % 26]
    return newString


test = "HELLOWORLD"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
