b,e =list(map(int,input("enter a base and exponential value with space:").split( )))
def power(b,e):
    if e == 0:
        return 1
    return b*power(b,e-1)
print(power(b,e))

# enter a base and exponential value with space: 2 3
# 8