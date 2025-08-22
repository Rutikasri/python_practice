def add(l1,l2):
    l1 = l1[::-1]
    l2 = l2[::-1]
    carry = 0
    result =[]
    i,j =0,0
    while i < len(l1) or j < len(l2) or carry:
        v1 = l1[i] if i < len(l1) else 0 
        v2 = l2[j] if j < len(l2) else 0
        total = v1 + v2 + carry
        carry = total//10
        result.append(total%10)
        i+=1
        j+=1
    return result[::-1] 
n1 = int(input("enter a size of list:"))
l1 = list(map(int,input("enter a numbers:").split()))
n2 = int(input("enter a size of list:")) 
l2 = list(map(int,input("enter a numbers:").split())) 
print(*add(l1,l2))      

#output

# enter a size of list:3
# enter a numbers:435
# enter a size of list:4
# enter a numbers:1354
# 1 7 8 9