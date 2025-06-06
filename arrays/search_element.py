def search_rotated(arr):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid]==target:
            return mid
        if arr[left] <= arr[mid]:
            if arr[left]<= target < arr[mid]:
                right = mid-1
            else:
                left = mid+1
        else:
            if arr[mid]<= target <= arr[right]:
                left = mid+1
            else:
                right = mid -1
    return -1 

arr = [1,2,8,3,5,7]
target = 8
print(search_rotated(arr))

#2