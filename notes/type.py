from collections import Counter


class Solution(object):
    def findLeastNumOfUniqueInts(arr,k):
        cnt = Counter(arr)
        freq = sorted(cnt.keys())
        for i in range(len(freq)):
            if k >= freq[i]:
                k -= freq[i]
                freq[i] = 0
            else:
                freq[i] -= k
                k = 0
                break
        return sum(1 for f in freq if f > 0)
                
    
        
print(Solution.findLeastNumOfUniqueInts([5,5,4],1))