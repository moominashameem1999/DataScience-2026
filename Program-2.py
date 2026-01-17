"""Write a Python program to implement a password retry system :
1. Set the correct password as "openAI123".
2. Allow the user 3 attempts to enter the password.
3. If the password entered is correct → print "Login Successful".
4. If the user fails in all 3 attempts → print "Account Locked"."""
password = "openAI123"
attempts = 0
while attempts < 3:
    user_password = input("Enter your password: ")
    if user_password == password:
        print("Login Successful")
        break
    attempts += 1
else:
    print("Account Locked")