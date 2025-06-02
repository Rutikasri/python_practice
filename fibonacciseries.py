# n = int(input())
# a,b =0,1
# print("series")

# for i in range(n):
#     if i == n-1:
#         print(a)
#     else:
#         print(a,end=', ')
#         c = a+b
#         a = b
#         b = c
        
N = int(input( ))
a,b = 0,1
for i in range(N+1):
  print(a,end =" ")
  a,b = b,a+b