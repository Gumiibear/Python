import string
kon = "bcdfghjklmnpqrstvwxz"

def rovarize(cleartext):
    rtext = ""
    for char in cleartext:
        if string.lower(char) in kon:
            rtext += char+"o"+char.lower()
        else:
            rtext += char
    return rtext

def derovarize(cipher):
    word = ""
    position = 0
    while position < len(cipher):
        word += cipher[position]
        if string.lower(cipher[position]) in kon \
                and string.lower(cipher[position]) == string.lower(cipher[position+2]):
            position += 2
        position += 1

    return word

print rovarize(cleartext="Hello")