n = int(input("enter a number:"))
if n <= 0:
    print(False)
else:
    while n % 3 == 0:
        n //= 3
    print(n == 1)

# enter a number:27
# True

# enter a number:28
# False