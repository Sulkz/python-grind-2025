def CapitaliseTitle(s: str):
    s = s.split()
    arr = []
    for words in s:
        words = words.lower()
        if len(words) <= 2:
            arr.append(words)
        else:
            arr.append(words.capitalize())
    return " ".join(arr)

print(CapitaliseTitle("haVe thE CAse in CART"))