def peak(arr):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if(mid==0 or arr[mid]>=arr[mid-1]) and (mid == len(arr)-1 or arr[mid] >= arr[mid+1]):
            return arr[mid]
        elif mid > 0 and arr[mid-1]>= arr[mid]:
            right = mid-1
        else:
            left = mid+1
            
arr = [12,34,23,56,42,43]
print(peak(arr))


#34