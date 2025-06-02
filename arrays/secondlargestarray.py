def second_largest_array(arr):
    arr = list(set(arr))
    if len(arr) < 2:
        return "second largest doesnot exist"
    
    arr.sort()
    return arr[-2]

numbers = [12,43,56,78,54,23 ]
print(second_largest_array(numbers))

#56