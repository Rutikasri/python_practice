def sum(*args):
    total = 0
    for num in args:
        if num % 2 == 0:
            total += num
    return total

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sum of even numbers:", sum(*numbers))


# Enter numbers separated by space: 1 2 3 4 3 5
# Sum of even numbers: 6