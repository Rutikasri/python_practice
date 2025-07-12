def gcd(a,b):
    if b ==0:
        return a
    return gcd(b,a%b)
a = int(input("enter first number:"))
b = int(input("enter second number:"))
print(gcd(a,b))

# enter first number:12
# enter second number:84
# 12