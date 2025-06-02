list = [32,57,24,67,43,23,25,67]
print(list)
element = list.pop(4)
print(list)
list.insert(2,element)
print(list)
list.append(element)
print(list)

# [32, 57, 24, 67, 43, 23, 25, 67]
# [32, 57, 24, 67, 23, 25, 67]
# [32, 57, 43, 24, 67, 23, 25, 67]
# [32, 57, 43, 24, 67, 23, 25, 67, 43]