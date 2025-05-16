def is_anagram(word1, word2):
    '''This function analyzes 2 words and determines if they are anagrams.'''
    gth = len(word1)
    gth2 = len(word2)
    emp = 0 
    if gth == gth2: 
        bank1 = list(word1)
        bank2 = list(word2)

        sorted_bank1 = sorted(bank1)
        sorted_bank2 = sorted(bank2)

        if sorted_bank1 == sorted_bank2:
            return True 
        else:
            return False 