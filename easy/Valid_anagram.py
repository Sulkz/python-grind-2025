from collections import Counter


def validAnagram(t,s):
    #super easy way = using Counters
    #return Counter(s) == Counter(t)
    
    #brute Force and not optimal at all
    letters = list(s)
    
    if len(s) != len(t):
        return False

    for char in t:
        if char not in letters:
            return False
        letters.remove(char)
    return True
