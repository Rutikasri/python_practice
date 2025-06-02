def word(sentence):
    words =sentence.split()
    return " ".join(reversed(words))
sen = input("enter a sentence:")
print(word(sen))