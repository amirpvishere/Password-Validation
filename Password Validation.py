# This is the most simple way to make a password validation with python
def password_validation(password):
    if len(password) < 8:
        print('Your password must contain at least 8 character')
    elif password.isnumeric():
        print('Your password must contain at least one character')
    elif password.isalpha():
        print('Your password must contain at least one number')
    elif password.islower():
        print('Your password must contain at least one upper letter')
    else:
        print('Your password has been created ')


while True:
    password = input('Enter your password: ')
    password_validation(password)
