n = int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(n,n-i,-1):
        print(j,end= " ")
    print()

# Enter the number of rows: 3
# 3 
# 3 2 
# 3 2 1 

