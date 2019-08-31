''' Q--
Python program to check the validity of a Password
In this program, we will be taking a password as a combination of alphanumeric characters along with special characters, and check whether the password is valid or not with the help of few conditions.

Primary conditions for password validation :

Minimum 8 characters.
The alphabets must be between [a-z]
At least one alphabet should be of Upper Case [A-Z]
At least 1 number or digit between [0-9].
At least 1 character from [ _ or @ or $ ].
Examples:

Input : R@m@_f0rtu9e$
Output : Valid Password

Input : Rama_fortune$
Output : Invalid Password
Explanation: Number is missing

Input : Rama#fortu9e 
Output : Invalid Password

'''

def checkEmail(email):
    ln = email._len_()
    if ln >2:
        dot_i = email.find(".")
        at_i = email.find("@")
        if dot_i != -1 and at_i != -1 and ln - dot_i > 2 and dot_i - at_i > 2 and ln - at_i >5 and at_i >2:
            return True
        else:
            return False
    else:
        return False
            
def checkPassword(pas):
    ln = pas._len_()
    if ln >8 and pas.isalnum() and pas.isprintable():
        return True
    else:
        return False        
            
                      

email = str(input("Enter Email :")).strip()
if checkEmail(email):
    print("Email is valid")
else:
    print("Invalid email address...!")
    
pas = str(input("Enter Password :")).strip()
if checkPassword(pas):
    print("Password is valid")
else:
    print("Week password")
