def gcd(a,b):
    while b!=0:
        a,b = b,a % b
    return a
a = int(input("enter a first number"))
b = int(input("enter a second number"))
print(gcd(a,b))