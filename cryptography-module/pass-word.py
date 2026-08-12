import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4.")
        return

    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    symbol = random.choice(string.punctuation)

    remaining = length - 4
    all_characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = [lowercase, uppercase, digit, symbol]

    for _ in range(remaining):
        password.append(random.choice(all_characters))

    random.shuffle(password)

    return "".join(password)

length = int(input("Enter password length: "))
password = generate_password(length)

if password:
    print("\nGenerated Password:", password)