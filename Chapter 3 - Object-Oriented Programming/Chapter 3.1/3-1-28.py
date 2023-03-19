#safe password verification
#string as argument
#True if following conditions are met
#at least eight characters long
#contains atleast 1 digit
#contains at least one uppercase letter
#contains at least one lowercase letter
#contains at least one character that is neither a letter nor a number

def passwordVerification(string=str):
    digits = [digit for digit in password if digit.isdigit()]             
    letters = [letter for letter in password if letter.isalpha()]                 
    if any(char.isspace() for char in string):
        return False
    if len(string) < 8:
        return False
    if  len(digits) < 1:
        return False
    if not any(letter.isupper() for letter in letters):
        return False
    if not any(letter.islower() for letter in letters):
        return False   
    if len(digits) + len(letters) < len(string):
        return True
    return False


password = 'hellomynameisKai1!'


print(passwordVerification(password))