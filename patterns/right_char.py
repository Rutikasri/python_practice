n = int(input("enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i):
        print(chr(65+j),end="")
    print()
    
# enter the number of rows: 5
#     A
#    AB
#   ABC
#  ABCD
# ABCDE