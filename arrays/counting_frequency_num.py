def count(arr):
    freq = { }
    for num in arr:
        if num in freq:
            freq[num] +=1
        else:
            freq[num] = 1
    return freq

arr = [1,2,3,1,2,3,4,5,4,6]
print(count(arr))

#{1: 2, 2: 2, 3: 2, 4: 2, 5: 1, 6: 1}