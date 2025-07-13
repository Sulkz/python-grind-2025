class Solution(object):
    def longestStrChain(words):
        # first sort words in ascending order
        words.sort(key=len)
        hashmap = {}
        
        for word in words:
            # this is for a word with only 1 character and the defualt for each words before finding chains
            hashmap[word] = 1
            # for each word we need to be removing each character so need another loop that actually interacts with the word
            for x in range(len(word)):
                #removing a character at each position
                #first removing the first character and then concatinating the other part 
                pred = word[:x] + word[x+1:]
                if pred in hashmap:
                    hashmap[word] = max(hashmap[word], hashmap[pred] + 1)
        return max(hashmap.values())
        
        
print(Solution.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))
# Expected: 4