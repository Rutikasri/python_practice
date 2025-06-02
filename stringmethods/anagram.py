def anagram(str1,str2):
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()
    if len(str1)!=len(str2):
        return "It is not a anagram"
    for char in str1:
        if str1.count(char) != str2.count(char):
            return "It is not a anagram"
    return "It is a anagram"
word1 = input("enter the first string:")
word2= input("enter the second string:")
print(anagram(word1,word2))
