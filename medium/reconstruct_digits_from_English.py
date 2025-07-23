from collections import Counter


class Solution(object):
    def convert(self,s):
        cnt = Counter(s)
        ans = {}
        # each word for 0-9 have distinct letters that can allow it to be identified
        ans[0] = cnt["z"]
        ans[2] = cnt["w"]
        ans[4] = cnt["u"]
        ans[6] = cnt["x"]
        ans[8] = cnt["g"]
        
        ans[1] = cnt["o"] - ans[2] -ans[4]
        ans[3] = cnt["h"] - ans[8]
        ans[5] = cnt["f"] - ans[4]
        ans[7] = cnt["v"] - ans[5]
        ans[9] = cnt["n"] - ans[1] - ans[7]
        
        output = ""
        
        for x in range(10):
            output += str(x) * ans[x]
        return output
    
    
