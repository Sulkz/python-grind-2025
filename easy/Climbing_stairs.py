# This is a dynamic programming question which requires memoisation if done
#  in recursion but is also just the fibonnacci sequence
def stairs(n: int) -> int:
    j,k = 1, 1
    for _ in range(n-1):
        temp = j
        j = j + k 
        k = temp
    return j

print(stairs(5))