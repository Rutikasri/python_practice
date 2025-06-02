def strongpassword(password):
    if(len(password)>8 and 
       any(char.isupper() for char in password) and
       any(char.islower() for char in password) and
       any(char.isdigit() for char in password) and
       any(char in "!@#$%^&*()" for char in password)):
        return True
    return False
passw = input("enter a password:")
print(strongpassword(passw))