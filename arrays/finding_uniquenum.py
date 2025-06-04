# arr = [1,2,2,1,4,5,6,3]
# unique = list(set(arr))
# print(unique)


def unique(arr):
    return list(set(arr))

arr = [1,2,2,1,4,3,5,6]
print(unique(arr))

#[1,2, 3, 4, 5, 6]