l1 = [1,3,4,5,6,4,2,3]
l2 = [6,9,3,7,2,7,9,2]
newlist = list()
odd = l1[1::2]
print(odd)
even = l2[0::2]
print(even)
newlist.extend(odd)
newlist.extend(even)
print(newlist)

# [3, 5, 4, 3]
# [6, 3, 2, 9]
# [3, 5, 4, 3, 6, 3, 2, 9]