def product(numbers):
    product = 1
    for num in numbers:
        product*=num
    return product
numbers=[2,5,6,9]
result = product(numbers)
print(result)