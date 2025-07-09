n = int(input("Enter the number of elements: "))
numbers = list(map(int,input("enter the numbers seperated by spaces:").split()))
count = 0
for num in numbers:
    if abs(num)>=1000:
        count+=1
print(count)


# Enter the number of elements: 5
# enter the numbers seperated by spaces:123 2342 3243 23 134533
# 3