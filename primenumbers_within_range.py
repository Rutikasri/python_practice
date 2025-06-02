start = int(input("enter a number: "))
end = int(input("enter the last number:"))
for num in range(start,end+1):
    if num > 1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)
            
# enter a number: 10 
# enter the last number:30
# 11
# 13
# 17
# 19
# 23
# 29