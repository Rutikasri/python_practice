n = int(input()) 
arr = []
for _ in range(n):
    arr.append(int(input()))
mid = n // 2
if n % 2 == 0:
    left = sorted(arr[:mid])
    right = sorted(arr[mid:])
    result = left + right
else:
    left = sorted(arr[:mid])
    middle = [arr[mid]]
    right = sorted(arr[mid+1:])
    result = left + middle + right
print(*result)
