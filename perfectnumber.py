num = int(input("enter a number:"))
sum = 0
for i in range(1,num):
    if num%i==0:
        sum+=i
if sum == num:
    print("it is a perfect number")
else:
    print("it is not a perfect number")
    
# enter a number:28
# it is a perfect number

# enter a number:15
# it is not a perfect number