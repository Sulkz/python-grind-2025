#reverse a string

s = "Hallo"
result = []
ls = list(s)
print(ls)

for i in range(len(s) - 1, -1, -1):
   letter = ls[i]
   result.append(letter)
print(''.join(result))

print(s[::-1])