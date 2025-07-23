"""
Requires sliding window with one pointer that needs to be moved manually utilising sets as well
"""
class Solution(object):
    def lengthOfLongestSubstring(s):
        memo = set()
        max_len = 0 
        lp = 0
        for rp in range(len(s)):
            while s[rp] in memo:
                #if the letter is already in the set then we reduce window by removing character at position lp
                memo.remove(s[lp])
                lp += 1
            memo.add(s[rp])
            #finding the lenght of the subarray window
            max_len = max(max_len, rp -lp + 1)
        return max_len
    
