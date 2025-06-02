def max(arr):
    max = arr[0]
    for num in arr:
        if num > max:
            max = num
    return max
arr = [12,34,65,86]
print(max(arr))