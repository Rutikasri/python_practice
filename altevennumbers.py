start = int(input())
end = int(input())
if start%2!=0:
    start+=1
else:
    start+=2
count = 0
for num in range(start,end,2):
    if count%2==0:
        print(num)
    count +=1
