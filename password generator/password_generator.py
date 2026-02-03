import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

length = int(input("Enter password length: "))
password = generate_password(length)
print("Your password is:", password)