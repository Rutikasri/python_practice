#multiply all numbers using nonlocal scope

def multiply(nums):
    result = 1  # outer variable
    def mul():
        nonlocal result  # refers to result from outer function
        for n in nums:
            result *= n
    mul()
    return result
num = list(map(int, input("enter a numbers with spaces:").split()))
print(multiply(num))

# enter a numbers with spaces:2 3 4 
# 24