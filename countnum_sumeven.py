def count(nums):
    count = 0
    for num in nums:
        num = abs(num)
        sum = 0
        while num > 0:
            sum += num % 10
            num = num // 10
        if sum % 2 == 0:
            count += 1
    return count
n = int(input("Enter the number of elements: "))
numbers = list(map(int, input("Enter the numbers separated by spaces: ").split()))
print(count(numbers))

# Enter the number of elements: 6
# Enter the numbers separated by spaces: 124 123 0845 435 23423 2324
# 3