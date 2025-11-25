username = input("Enter the username: ")
password = input("Enter the password: ")

if (username == "admin" and password == "pass"):
    print("Login Successful!")
elif(username != "admin"):
    print("Wrong Username")
else:
    print("Wrong Password")

