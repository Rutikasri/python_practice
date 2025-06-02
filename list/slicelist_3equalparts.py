list1 = [1,3,5,7,3,8,9,4,2]
length = len(list1)
chunk_size = int(length/3)
start = 0
end = chunk_size
for i in range(3):
    indexes = slice(start,end)
    list_chunk = list1[indexes]
    print("chunk",i,list_chunk)
    print("reversing list",list(reversed(list_chunk)))
    start = end
    end +=chunk_size
    
    
# chunk 0 [1, 3, 5]
# reversing list [5, 3, 1]
# chunk 1 [7, 3, 8]
# reversing list [8, 3, 7]
# chunk 2 [9, 4, 2]
# reversing list [2, 4, 9]