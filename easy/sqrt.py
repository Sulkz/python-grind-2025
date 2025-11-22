def sqrt(x: int) -> int:
    l, r = 0, x // 2
    while l <= r:
        mid = l+(r-l)//2
        sq = mid**2
        if sq == x:
            return mid
        elif sq < x:
            l = mid + 1
        else:
            r = mid - 1
    #we want to return the largest number that is less than the square root
    return r 

print(sqrt(8))
