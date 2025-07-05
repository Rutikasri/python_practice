num = int(input("enter a number:"))
square = num*num
sum =0
while square >0:
    digit = square%10
    sum+=digit
    square //=10
if sum==num:
    print("it is neon number")
else:
    print("it is not neon number")
    
# enter a number:9
# it is neon number