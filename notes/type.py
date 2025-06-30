def say_Goodbye():
    print("byebye my broder! back to theh lobby")
    
say_Goodbye()

def multiply(x,y):
    total = x * y
    return total

print(multiply(10,10))

def twosum(a,b,c):
    return (a + b + c)
    
    
result = twosum(5,14,6)
print(result)

def typinting(name: str,car : str) -> None:
    print ("This car is " + name + " from here  " + car)

typinting("honda", "Accrod")


for c in reversed(range(1,11)):
    print(c)
    
    
def concatenate(s1: str, s2: str) -> str:
    concat = s1 + s2
    if len(concat) > 10:
        return("Too long dawg")
    return concat

print(concatenate("He", "llo"))
print(concatenate("Goodbye", "Ngor"))


def sliced_string(s1: str, n: int, k: int)->str:
    if k >= len(s1):
        return ""
    sliced = s1[n:k]
    return sliced

print(sliced_string("Hello gallow",1,100))

def reversing_String(s1: str, n: int):
    result = s1[::n]
    return result

print(reversing_String("gallo",-1))
print(reversing_String("gallo",-2))

# def change_word(word: str, n: int):
#     cut = word[:n]
#     replacement = input("Gimme something: ")
#     together = cut + replacement
#     return together

# print(change_word("click ways",5))




# def format_msg()->str:
#     name = input("Input your name: ")
#     age = input ("How old are you: ")
#     feedback = "Hello {} my child, what brings.\nYou here young padowan, oh wait ur how old? {} !! stop right there dawg!".format(name,age)
#     return feedback

# print(format_msg())

# pairs = [(2, 3), (1, 5), (4, 1)]

# pairs.sort(key=lambda num: num[1], reverse=False)

# print(pairs)

# # Sort words = ["hello", "world", "python", "a", "banana"] by length descending

# words = ["hello", "world", "python", "a", "banana"]

# words.sort(key=lambda phrases : len(phrases), reverse=True)

# print(words)


# nums = list(range(100))    
# even = list(filter(lambda num : num % 2 == 0, nums))

# print(even)
# \
    
word = "sliceme"

print(word[0:3])
