# The number of rows for the pyramid should be provided as input at runntime
# The program should only print the pattern and no unnecessary messages or prompts
# The pattern should consist of:
# An upper part that forms a right-aligned pyramid,
# A lower part that mirrors the upper part

n = int(input("enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"*"*i)
    
# enter the number of rows:3
#   *
#  **
# ***
#  **
#   *