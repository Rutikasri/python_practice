#filter multiples of 3 using lambda and filter(with falling back messege)

nums = list(map(int,input("enter a numbers with spaces:").split( )))
multiples = list(filter(lambda x:x%3==0,nums))
if multiples:
    print("Multiples of 3 are:",*multiples)
else:
    print("No multiples of 3 found in the list.")
    
# enter a numbers with spaces:12 32 24 18 20
# Multiples of 3 are: 12 24 18