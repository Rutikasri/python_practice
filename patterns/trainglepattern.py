r = int(input())
if r<0:
    print("invslid input")
elif r ==0:
    print("zero")
else:
    for i in range(1,r+1):
        spaces = ' '*(r-i)
        stars = '* '*i
        print(spaces+stars)
        
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * *