list1 = list(map(int, input("Enter numbers: ").split()))
newlist = list(reversed(list1))
print(*newlist)

# Enter numbers: 1 2 3 4 5
# 5 4 3 2 1

# list1 = list(map(int, input("Enter numbers: ").split()))
# newlist = list(reversed(list1))
# print(newlist)

# Enter numbers: 1 2 3 4 5
# [5, 4, 3, 2, 1]