def duplicates(arr):
    seen = set( )
    duplicates = set( )
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

input = [1,2,3,1,3,4,2,5,5,6]
print(duplicates(input))

#[1, 2, 3, 5]