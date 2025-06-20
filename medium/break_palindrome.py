"""
Break a Palindrome
https://leetcode.com/problems/break-a-palindrome
"""

class Solution(object):
    def breakPalindrome(self, palindrome):
        s = list(palindrome)
        length = len(palindrome)
        
        #for cases where palindrone is single "a" or "b"
        if length <= 1:
            return ""
        
        for x in range(length // 2):
            if s[x] != "a":
                s[x] = "a"
                return ''.join(s)
        #we chose the last as this will make the string lexically smaller than "aa"   
        s[-1] = "b"
        return ''.join(s)
        
        
      
                

