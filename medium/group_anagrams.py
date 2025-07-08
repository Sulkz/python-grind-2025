
from collections import defaultdict


class Solution(object):
    def groupAnagrams(strs):
        #dictionary for the group
        phrases = defaultdict(list)
        for words in strs:
            #for anagrams they have to contain all the letters so we use a sorted tuple  and then append
            key = tuple(sorted(words))
            # for a specific key of letters, the words are grouped
            phrases[key].append(words)
        return phrases.values()
    

print(Solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))