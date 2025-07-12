#recursion
def product(n):
    if n == 0:
        return 0
    if n < 10:
        return n
    return (n % 10) * product(n // 10)
n = int(input("enter a number:"))
print(product(n))
  
# enter a number:234
# 24