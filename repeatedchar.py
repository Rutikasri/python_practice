#find the first repeated char in a given string.if there is no repeated char return none

n = input("enter a string: ")
count ={ }
for i in n:
    if i in count:
        print(i)
        break
    else:
        count[i]=1
else:
    print("none")
    
# enter a string: hellogeeks
# l