n = int(input("enter the number of rows:"))
half =n//2
for i in range(1,half+1):
    print("*"*i + " "*(2*(half-i))+"*"*i)
for i in range(half,0,-1):
    print("*"*i + " "*(2*(half-i))+ "*"*i)
    
# enter the number of rows:6
# *    *
# **  **
# ******
# ******
# **  **
# *    *