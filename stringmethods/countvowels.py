def counting(s):
    vowles = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowles:
            count+=1
    return count
s = input("enter a string:")
print(counting(s))