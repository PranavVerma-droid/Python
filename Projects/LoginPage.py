print('Welcome to the Router Login Page! Please Enter your Username and Password to Login.')
x = str(input('Enter your Username: '))
y = str(input('Enter your Password: '))

correct_username = 'admin'
correct_password = 'password'


if (x == correct_username and y == correct_password):
    print('Login Successful')
else:
    print('Login Failed, Please Try Again!')
