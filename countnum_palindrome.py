def count(nums):
    count = 0
    for num in nums:
        num = str(abs(num))
        if num == num[::-1]:
            count+=1
    return count
n = int(input("Enter the number of elements: "))
numbers = list(map(int, input("Enter the numbers separated by spaces: ").split()))
print(count(numbers))

# Enter the number of elements: 5
# Enter the numbers separated by spaces: 123 11011 123 313 2334
# 2