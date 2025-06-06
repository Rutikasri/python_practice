def min(arr):
    left = 0 
    right = len(arr)-1
    while left < right:
        mid = (left+right)//2
        if arr[mid]>arr[right]:
            left = mid+1
        else:
            right = mid
            
    return arr[left]

arr = [10,20,30,40,50]
print(min(arr))

#10