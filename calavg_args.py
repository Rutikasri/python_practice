#calculate the average of numbers using args
#use a function that accepts a variable number of arguments using *args

def average(*args):
    if len(args) == 0:
        return 0
    total = sum(args)
    avg = total / len(args)
    return avg

nums = list(map(int, input("enter a numbers with spaces: ").split()))
print("Average is:", average(*nums))
 
# enter a numbers with spaces: 10 20 30 40 50
# Average is: 30.0