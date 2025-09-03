
def largest_two_digits_from_string(s):
    maxim = -float("inf")
    for x in range(len(s)-1):
        nums = int(s[x:x+2])
        maxim = max(maxim, nums)
    return maxim
        

print(largest_two_digits_from_string("17129310"))