#running total using global scope

total =0
def sum(num):
    global total
    total += num
    return total
num = list(map(int,input("enter a numbers with spaces:").split( )))
for i in num:
    print("total: ",sum(i))


# enter a numbers with spaces:5 10 15
# total:  5
# total:  15
# total:  30