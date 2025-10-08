def isPlaindrome(self, s:str):
    res = []
    for char in s:
        if char.isalnum():
            res.append(char.lower())
    s = "".join(res)
    return s == s[::-1]

print(isPlaindrome(isPlaindrome, "Was it a car or a cat I saw?"))