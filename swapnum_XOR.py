a = int(input("enter a number: "))
b = int(input("enter another number: "))
a = a ^ b
b = a ^ b
a = a ^ b
print("After swapping:")
print("a =", a)
print("b =", b)

# enter a number: 3
# enter another number: 5
# After swapping:
# a = 5
# b = 3