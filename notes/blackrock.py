def commonSets (set1, set2):
    memo = {}
    sim = []
    for letters in set1:
        memo[letters] = letters
    for x in set2:
        if x in memo:
            sim.append(x)
    if sim:
        sim.sort()
        return sim
    else:
        return 'NULL'
            
    
    
            
print(commonSets(set(['1','2','3', 'A', 'B', 'C']),set(['j','2','3', 'A', 'B', 'C'])))