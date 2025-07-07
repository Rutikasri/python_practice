n = 6 
for i in range(1, n + 1):
    print(" " * (i - 1), end="")
    for j in range(i, n + 1):
        print(j, end=" ")
    print()
for i in range(n - 1, 0, -1):
    print(" " * (i - 1), end="")
    for j in range(i, n + 1):
        print(j, end=" ")
    print()
    
# 1 2 3 4 5 6 
#  2 3 4 5 6 
#   3 4 5 6
#    4 5 6
#     5 6
#      6
#     5 6
#    4 5 6
#   3 4 5 6
#  2 3 4 5 6
# 1 2 3 4 5 6