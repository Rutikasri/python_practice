# n = int(input("enter a number"))
# count = 0
# num = 2
# primes =[ ]
# while count < n:
#     is_prime = True
#     if num < 2:
#         is_prime = False
#     else:
#         for i in range (2,int(num**0.5)+1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#     if is_prime:
#         primes.append(num)
#         count +=1
#     num+=1
# print(", ".join(map(str,primes)))


n = int(input("Enter a number : "))
count = 0
num = 2

while count < n:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=' ')
        count += 1
    num += 1


# Enter a number : 8
# 2 3 5 7 11 13 17 19  