
"""
Utilisies 2Sum formula of chekcin if we have seen a value however doesnt need to have allota
info like 2 sum whcih has to store the indexes
"""
class Solution(object):
    def containsDuplicate(self, nums):
        #can use a set or hashmap (set in this case as we only need the element and to recognise if num inside already)
        memo = set()
        for n in nums:
            #checks its first if its already there and then returns true
            if n in memo:
                return True
            #else add it to memo as it has not been seen yet
            memo.add(n)
        return False