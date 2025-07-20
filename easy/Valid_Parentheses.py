class Solution(object):
    def isValid(s):
        memo = {")":"(", "]":"[", "}":"{"}
        stack = []
        for char in s:
            # this checks the openings
            if char in memo.values():
                stack.append(char)
            # this checks the endings
            elif char in memo.keys():
                # checks if its empty and then checks if the value for the dictionary is not
                # equal to the one that is poped out these all check if it doesnt equal
                if not stack or memo[char] != stack.pop():
                    return False
        return not stack
    
    
print(Solution.isValid("([]})"))
                    
            