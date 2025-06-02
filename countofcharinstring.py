def charcount(s):
    newcharcount={ }
    for char in s :
        newcharcount[char] = newcharcount.get(char,0)+1
    return newcharcount
str = "RutikaSri"
result = charcount(str)
print(result)