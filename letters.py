import string
def count_letters(file):
    '''This function counts the number of the given file.'''
    thisdict = {}          #initialize dictionary 



    f = open(file)
    for line in f:
        for char in line.lower():
            if char.isalpha() and char.isascii() and char.lower() in string.ascii_lowercase:
                letter = char.lower()
                thisdict[letter] = thisdict.get(letter, 0)+1

                """Checks if the character is a lowercase letter."""
    f.close()
    return thisdict