def anagram (str1,str2):
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()
    
    return sorted(str1) == sorted(str2)

word1 = input("enter the first string:")
word2 = input("enter the second string:")

print(anagram(word1,word2))
        