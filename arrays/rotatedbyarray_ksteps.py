def rotated_array(arr,k):
    n = len(arr)
    k = k % n 
    return arr[-k:] + arr[:-k]
arr = [1,2,4,3,7,4,7]
k = 3
print(rotated_array(arr,k))

#[7, 4, 7, 1, 2, 4, 3]