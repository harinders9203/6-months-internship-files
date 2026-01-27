import re

password = input("Enter password: ")

if len(password) < 8:
    print("Weak password: Too short")

elif not re.search("[A-Z]", password):
    print("Weak password: No uppercase letter")

elif not re.search("[a-z]", password):
    print("Weak password: No lowercase letter")

elif not re.search("[0-9]", password):
    print("Weak password: No digit")

elif not re.search("[^A-Za-z0-9]", password):
    print("Weak password: No special character")

else:
    print("Strong password")