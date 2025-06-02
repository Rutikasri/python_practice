def convert(n):
    num ={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten"}
    result = ""
    for digit in str(n):
        result += num[int(digit)] + " "
    return result.strip()
n = int(input("enter a number:"))
print(convert(n))
