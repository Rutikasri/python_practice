num = int(input("enter a number:"))
sum =0
product =1
while num>0:
    digit = num%10
    sum += digit
    product *=digit
    num //=10
if sum == product:
    print("it is a spy number")
else:
    print("it is not a spy number")
    
# enter a number:1124
# it is a spy number

# enter a number:1234
# it is not a spy number

