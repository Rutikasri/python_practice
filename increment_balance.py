n = int(input("enter the no of digits:"))
digits =list(map(int,input().split()))
carry = 1
for i in range(n-1,-1,-1):  #This for loop goes backward through the list (from last digit to first digit).If n = 3, then it goes through indexes 2, 1, 0.
    newdigit = digits[i]+carry
    digits[i] = newdigit % 10
    carry = newdigit//10
if carry:
    digits = [carry] + digits
print(*digits)
    