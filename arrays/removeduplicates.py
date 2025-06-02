def remove(arr):
    unique = [ ]
    for num in arr:
        if num not in unique:
            unique.append(num)
    return unique
arr = [1,2,4,2,5,3,6,3]
print(remove(arr))

#[1, 2, 4, 5, 3, 6]