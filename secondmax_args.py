#find second maximum number in a list using args

def maximum(*args):
    unique = list(set(args))
    if len(unique)<2:
        return "not enough unique numbers"
    unique.sort(reverse=True)
    return unique[1]
nums = list(map(int, input("Enter numbers with spaces: ").split()))
print("Second maximum is:", maximum(*nums))


# Enter numbers with spaces: 10 40 23 60 70 30
# Second maximum is: 60