correct_username = 'admin'
correct_password = '123'
max_attempts = 3
while True: 
    username = input('Enter your Username: ')
    password = input("Enter your password: ")
    if username == correct_username and password == correct_password:
        print("Login Successfully!")
        break
    else:
        max_attempts -= 1
        print(f"Incorrent password, remaining attempts: {max_attempts}")
    if max_attempts == 0:
        print("Account locked for security.")